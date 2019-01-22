import pymongo

import configuration as config

__mongo_collection = None


def initialize_mongo():
    global __mongo_collection

    __mongo_client = pymongo.MongoClient(config.MONGO_HOST, config.MONGO_PORT)
    __mongo_database = __mongo_client[config.MONGO_DATABASE]
    __mongo_collection = __mongo_database[config.MONGO_COLLECTION]


def submit_action(request_data):
    result = __mongo_collection.insert_one(request_data)
    return result.acknowledged


def get_results(filter_criteria=None, projection=None, skip=None, limit=None):
    if limit is None or limit > config.MONGO_MAX_RETRIEVAL:
        limit = config.MONGO_MAX_RETRIEVAL
    results = list(__mongo_collection.find(filter=filter_criteria, projection=projection, skip=skip, limit=limit))
    return results
