import time, json, requests
from typing import Union
from requests.models import Response

KONG_HOST = 'gateway' # 0.0.0.0 | gateway | localhost
KONG_ADMIN_PORT = 8001
KONG_PROXY_PORT = 8002
KONG_ADMIN_URL = f"http://{KONG_HOST}:{KONG_ADMIN_PORT}"
KONG_PROXY_URL = f"http://{KONG_HOST}:{KONG_PROXY_PORT}"
URL = 'https://calendrier.api.gouv.fr/jours-feries/metropole.json'
TEST = {
    'name': 'api-earthquakes',
    'host': 'http://api:8000',
    'paths[]': '/api',
    'route_name': 'FastAPI',
    'consumer': 'ito'
}

# Functions
def define_service(data: dict) -> requests.Response:
    """
    Define a kong service.

    :param data: (dict) 'url' and 'name' are necessary keys in dict.
    :return: requests.Response
    """

    assert 'url' in data.keys()
    assert 'name' in data.keys()

    return requests.post(f"{KONG_ADMIN_URL}/services/", data=data)

def define_route(data: dict, name: str) -> requests.Response:
    """
    Define a kong route.

    :param data: (dict) 'paths[]' is a key in dict.
    :param name: (str) name of the service linked to this route
    :return: requests.Response
    """

    assert 'paths[]' in data.keys()

    return requests.post(f"{KONG_ADMIN_URL}/services/{name}/routes", data=data)

def create_consumer(username: str) -> requests.Response:
    """
    Create a consumer.

    :param username: (str) username of the new consumer
    :return: requests.Response
    """
    data = dict(username=username)

    return requests.post(f"{KONG_ADMIN_URL}/consumers/", data=data)

def get_consumer_key(username: str) -> Union[str, None]:
    """
    Get a consumer's API key.

    :param username: (str) username of consumer
    :return: requests.Response
    """

    response = requests.post(f"{KONG_ADMIN_URL}/consumers/{username}/key-auth")

    # Error in request
    if response.status_code != 201:
        return None
    
    # Get API key
    api_key = response.json()['key']

    return api_key

def define_route_apikey(key_names: str, service_id: str, name: str='key-auth') -> requests.Response:
    """
    Define an API key for a route

    :param key_names: corresponds to config.key_names
    :param service_id: corresponds to the service id
    :return: requests.Response
    """
    data = {'name': name, 'config.key_names': key_names}
    url = f"{KONG_ADMIN_URL}/services/{service_id}/plugins"

    return requests.post(url, data=data)

def setup_service(data: dict) -> bool:
    # Define service
    data_service = dict(name=TEST['name'], url=TEST['host'])
    service_route = define_service(data_service)

    # Failed to create the service
    if service_route.status_code != 201:
        return False

    # Extract new service ID
    service_id = service_route.json()['id']

    # Define route
    data_route = {'paths[]': TEST['paths[]'], 'name': TEST['route_name']}
    route_response = define_route(data_route, name=data_service['name'])

    # Failed to create the route
    if route_response.status_code != 201:
        return False

    return True

def kong_is_ready():
    try:
        res = requests.get(f"{KONG_ADMIN_URL}/")
        return res.status_code == 200
    except Exception as e:
        return False 

def setup_services(filename: str) -> bool:
    # Read file
    f = open(filename, 'r')
    services = json.load(f)

    # Wait for Kong gateway to be ready
    while True:
        if kong_is_ready():
            break
        else:
            time.sleep(10)

    # Loops over the services
    for service in services:
        # Case the service setup failed
        if not setup_service(service):
            print(f"Failed to setup service for {service['name']}.")
            f.close()
            return False

    # Close file
    f.close()

    return True

# Test functions
def test_service():
    # Define service
    data_service = dict(name=TEST['name'], url=TEST['host'])
    service_route = define_service(data_service)

    if service_route.status_code >= 300:
        print(f"> Error: {service_route.json()}")
        return
    else:
        print(f"   Response {service_route.json()}\n")

    service_id = service_route.json()['id']
    print(f"> Service '{data_service['name']} was created (ID={service_id})'\n")

    # Define route
    data_route = {'paths[]': TEST['paths[]'], 'name': TEST['route_name']}
    route_response = define_route(data_route, name=data_service['name'])
    print(f"> Route (ID={route_response.json()['id']}) for '{data_service['name']}' was created.\n")

    # Try
    test_url = f"{KONG_PROXY_URL}/{TEST['paths[]'][1:]}/db/earthquakes/find?limit=1"
    print('> URL:', test_url)
    response = requests.get(test_url)
    print('> GET Test service:', response.json(), '\n')

    # # Define consumer & get API key
    # consumer = TEST['consumer']
    # _ = create_consumer(consumer)
    # api_key = get_consumer_key(consumer)
    # print(f"> {consumer} was created (API KEY={api_key}).", '\n')
    # _ = define_route_apikey('apikey', service_id)

    # # Try service w/ key
    # headers = {'apiKey' : api_key}
    # test_url2 = f"{KONG_PROXY_URL}/{TEST['paths[]'][1:]}/db/earthquakes/find?limit=1"
    # response = requests.get(test_url2, headers=headers)
    # print('> URL:', test_url2)
    # print(f'> GET {consumer} w/ API KEY:', response.json(), '\n')
    return True

if __name__ == '__main__':
    result = setup_services('services.json')
    print(f"Services setup was {'' if result else 'un'}successful")
