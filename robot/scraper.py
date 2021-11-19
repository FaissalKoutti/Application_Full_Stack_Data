# External packages
from datetime import timedelta, datetime
from http import HTTPStatus
import threading
import requests
import json
import logging
import os

# Constants
GATEWAY_URL = os.environ.get('GATEWAY_URL')
QUERY_URL = os.environ.get('QUERY_URL')
DATE_OUTPUT_FORMAT = "%Y-%m-%d"
INSERT_URL = os.environ.get('INSERT_URL')

# Functions
def datetime_to_string(date: datetime) -> str:
    """
    Return a ISO 8601 format string representing a date.

    :date: (datetime.datetime) the date
    :return: string represntation in ISO-8601
    :rtype: (str)
    """

    return date.strftime(DATE_OUTPUT_FORMAT)

def prepare_url() -> str:
    """
    Prepare the query url for the data by giving a start date and
    end date.

    :return: url
    :rtype: (str)
    """
    # Prepare the date
    month_ago = datetime.now() - timedelta(weeks=4)
    date = datetime_to_string(month_ago)

    # Change the url
    return f"{QUERY_URL}&starttime={date}"

def get_data() -> list:
    """
    Returns a list of elements extracted from REST API with url.

    :return: List of most likely dictionaries or empty list
    :rtype: (list)
    """
    # Variables initialization
    data = list()
    url = prepare_url()

    # POST request
    response = requests.get(url)

    # Extract data if requests was successful
    if response.status_code == HTTPStatus.OK:
        data = response.json()['features']

    return data

def set_interval(func, sec: int):
    """
    Launch the given function at given interval.

    :param funct: the function
    :param sec: (int) the interval/frequency
    """
    def func_wrapper():
        func()
        set_interval(func, sec)

    t = threading.Timer(sec, func_wrapper)

    t.start()

    return t

def process_element(element: dict) -> dict:
    """
    Change some properties of the element.

    :param element: element
    :rtype: (dict)
    :return: modified element
    """
    modified = element

    modified['_id'] = element['id']

    return modified

def insert_element(element: dict) -> bool:
    """
    Insert an element to the database.

    :param element: element to add 
    :return: a bool indicating the insert result
    :rtype: (bool)
    """
    # Process the element
    processed_element = process_element(element)

    # Launch POST request
    response = requests.post(
        INSERT_URL,
        data=json.dumps(processed_element)
    )

    return response.status_code < 300

def gateway_connected() -> bool:
    try:
        requests.get(GATEWAY_URL)
        return True
    except:
        return False

def pipeline() -> int:
    """
    Get the data and insert it to database with API and return
    the number of data inserted.
    """
    success: int = 0
    no_problem: bool = False

    # Get the data
    data = get_data()

    # Check gateway is ready
    while not no_problem:
        if gateway_connected():
            print("Gateway ready.")
            break

    # Insert elements
    for element in data:
        logging.info(f"pipeline: elements are being inserted ({success}).\r")
        inserted = insert_element(element)
        success += 1 if inserted else 0

    logging.info(f"pipeline: {success} elements were inserted.")
    
    return success
