import os
from pymongo import MongoClient


def register_analysis(analysis_object: dict) -> None:
    cluster = MongoClient(os.getenv("MONGO_URI"))
    db = cluster['music']
    collection = db['analysis']

    collection.insert_one(analysis_object)
