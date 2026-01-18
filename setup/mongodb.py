from pymongo import MongoClient
from .settings import MONGO_SETTINGS

def get_mongo_connection():

    client = MongoClient(
        host=MONGO_SETTINGS['mongo_host'],
        port=int(MONGO_SETTINGS['mongo_port'])
    )

    return client[MONGO_SETTINGS['mongo_db']]