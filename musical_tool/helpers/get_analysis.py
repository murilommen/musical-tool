import os

import pymongo 

    
client = pymongo.MongoClient(os.getenv("MONGO_URI"))     

db = client["music"] 
col = db["analysis"] 

lista_de_jsons = []

# Quando não quiser algum parametro, passe 0 -> exemplo: "_id": 0
for document in col.find({}, 
    {"_id": 0, 
     "music": 1, #"Performance1_G1", 
     "musicAnalysis": 1, 
     "group": 1, 
     "name": 1,
     "params": 1
    }): 
    lista_de_jsons.append(document)


print(lista_de_jsons)