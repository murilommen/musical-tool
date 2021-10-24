import os
from pymongo import MongoClient


def register_analysis(analysis_object: dict) -> None:
    cluster = MongoClient(os.getenv("MONGO_URI"))
    db = cluster['music']
    collection = db['analysis']

    collection.insert_one(analysis_object)


def list_musics() -> dict:
    base_url = "https://github.com/murilommen/musical-tool/blob/main/music_files/"
    musics_list = os.listdir("./music_files")

    musics_object_list = []

    for music in musics_list:
        music_string = base_url + music
        musics_object = {}
        musics_object["music"] = os.path.splitext(music)[0]
        musics_object["path"] = music_string
        musics_object_list.append(musics_object)

    return musics_object_list
