import json
from pymongo import MongoClient

try:
    # create a client objet to access to database;
    dbClient = client = MongoClient('localhost', 27017)
    # open a connection to the database trocdb
    db = dbClient["trocdb"]
    # access or create a collection named dataset
    collection = db["users"]
    # drop collection if it exists
    collection.drop()
    
except:
    print("dbMessage: Connection failed!")
else:
    print("dbMessage: Connection succes!")
    try:
        # load file dataset into 
        with open("collection.json") as jsObject:
            mongoDocument = json.load(jsObject)
        collection.insert_many(mongoDocument)

    except:
        print("dbMessage: dataset.json file not found")
    else:
        print("dbMessage: dataset.json file load succesfully!")



# use to print collection content
# for x in collection.find():
    # print(x) 









