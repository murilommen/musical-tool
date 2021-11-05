import os
import json
from pymongo import MongoClient


def register_analysis(analysis_object: dict) -> None:
    cluster = MongoClient(os.getenv("MONGO_URI"))
    db = cluster['music']
    collection = db['analysis']

    collection.insert_one(analysis_object)


def list_musics() -> dict:
    with open("musics.json", "r") as f:
        musics_dict = json.load(f)

    musics_object_list = musics_dict["analysis_list"]
    return musics_object_list
