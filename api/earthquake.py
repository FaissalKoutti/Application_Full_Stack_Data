# External packages
import pymongo

# Functions
MONGO_URI = 'mongodb://mongodb:27017/'
EARTHQUAKE_COLLECTION = 'earthquakes'

def get_collection(database: str, collection: str):
    # Connect
    client = pymongo.MongoClient(MONGO_URI)

    # Link with the database
    database = client[database]

    # Link with the collection
    collection = database[collection]

    return collection

def get_earthquakes(database: str, limit: int, min_magnitude: float=None, max_magnitude: float=None, tsunami: bool=None) -> list:
    # Prepare filter
    filter_query = dict()

    if min_magnitude and max_magnitude:
        filter_query['$and'] = [
            {'properties.mag': {'$gte': min_magnitude}},
            {'properties.mag': {'$lte': max_magnitude}}
        ]

    elif min_magnitude:
        filter_query['properties.mag'] = {'$gte': min_magnitude}

    elif max_magnitude:
        filter_query['properties.mag'] = {'$lte': max_magnitude}

    if tsunami:
        filter_query['properties.tsunami'] = (tsunami == True)

    # Connect to collection
    collection = get_collection(database, EARTHQUAKE_COLLECTION)

    # Get elements
    earthquakes = [_ for _ in collection.find(filter_query).limit(limit).sort("properties.time", pymongo.DESCENDING)]

    return earthquakes

def insert_earthquake(database: str, earthquake: dict):
    # Connect to collection
    collection = get_collection(database, EARTHQUAKE_COLLECTION)

    # Check if earthquake is already in database
    if collection.find_one({'_id': earthquake['_id']}) is None:
        # Update the earthquake in database
        collection.insert_one(earthquake)
    else:
        # Add the earthquake in database
        collection.replace_one({'_id': earthquake['_id']}, earthquake)
    
    return True

def get_earthquakes_count(database: str, min_magnitude: float=None) -> int:
    # Connect to collection
    collection = get_collection(database, EARTHQUAKE_COLLECTION)

    if min_magnitude:
        collection = collection.find({"properties.mag": {"$gte": min_magnitude}})

    return collection.count()

def get_earthquakes_aggregation(database: str, type_agg: str) -> float: 
    """
    
    :param database: (str)
    :param type_agg: (str) Either 'avg', 'max'
    """
        # Connect to collection
    collection = get_collection(database, EARTHQUAKE_COLLECTION)

    # Get elements
    earthquakes = list(collection.aggregate([{'$group': {'_id': 'null', type_agg: {f'${type_agg}': '$properties.mag'}}}]))

    return earthquakes
