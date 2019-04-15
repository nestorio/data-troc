import datetime
from pymongo import MongoClient

def getCollectionInstance():
    """" Returns an instance of our collection like driver to manage our db """
    try:
        # create a client objet to access to database;
        dbClient = client = MongoClient('localhost', 27017)
        # open a connection to the database trocdb
        db = dbClient["trocdb"]
        # access or create a collection named users
        collection = db["users"]
    except:
        print("dbMessage: Collection Access failed!")
    else:
        print("dbMessage: Collection Access succes!")
        return collection


# this global variable or objet
# will be use by all function which need to access to the database
collection = getCollectionInstance()


def sendMessage(receiver: str = "isaac2houngue", content: str = "le temps passe") -> None:
    """ Write to send message to someone who has initiated a troc """
    connectedUserEmail = "wpulver0@pen.io"
    contextObjectId = "fake1d"

    # object condition for selecting document
    conditionObjet = {
        "email": connectedUserEmail
    }
    for document in collection.find(conditionObjet):
        messageList = document["messages"]
        messageList.append({
            "content": content,
            "receiver": receiver,
            "date": datetime.datetime.now(),
            "contextObjectId": conditionObjet
        })
        collection.update_one(conditionObjet, {"$set":
            {
                "messages": messageList
            }
        })
    for x in collection.find(conditionObjet):
        print(x)
    return None


# ---------------------------------------------------------------------------
def getObjectId(owner: str = "", date="") -> str:
    """ This function is a helper for getting the id of any object knowing its owner and posted date """
    conditionObjet = {

    }
    return ""

def getTroquingObjectId(categorie, ville, value) -> str:
    return ""


def addObject(name, description, value, category, imageName, ville, isTroc, connectedUserEmail):
    contextObjectId = "fake1d"
    # isTrue:bool=False
    conditionObjet = {
        "email": connectedUserEmail
    }

    for document in collection.find(conditionObjet):
        objectList = document["objects"]
        objectList.append({
            "name": name,
            "category": category,
            "value": value,
            "ville": ville,
            "description": description,
            "isTroc": isTroc,
            "imageName": imageName
        })

        collection.update_one(conditionObjet, {"$set":
            {
                "objects": objectList
            }
        })

    for x in collection.find(conditionObjet):
        print(x)

    return None


def loginUser(email, password):
    myquery = {"email": email, "password": password}
    #print(myquery)

    mydoc = collection.find(myquery)
    #mydb.system.indexes.find()
    counter = 0
    for x in mydoc:
        first_name = x['first_name']
        email = x['email']
        client_Id = str(x['_id'])
        counter = counter + 1

    clientDetails ={"first_name": "", "client_Id": ""}
    if(counter == 1):
        #print("My first name is: "+ first_name + " and my id is: "+client_Id)
        clientDetails = {"first_name":first_name, "client_Id":client_Id, "email":email}

    return clientDetails
def userExist(email):
    myquery = {"email": email}
    mydoc = collection.find(myquery)
    counter = 0
    rclientExist = False
    for x in mydoc:
        counter = counter + 1

    if (counter >= 1):

        rclientExist = True

    return rclientExist

def registerClient(data):
    mydict = {
        "lastname": data['lastname'],
        "firstname": data['firstname'],
        "address": data['address'],
        "telephone": data['telephone'],
        "password": data['password'],
        "email":data['email'],
        "messages": [],
        "objects": [],
        "date_manager": []
    }

    x = collection.insert_one(mydict)
    return True


def searchIsTrocObject(category: str = "", ville: str = "", all: bool = False) -> list:
    """ For research """
    objectList = []
    if all:
        for document in collection.find():
            objectList.extend(document["objects"])
        print(objectList)
    else:
        for document in collection.find():
            if not document["objects"]:
                continue
            else:
                for object in document["objects"]:
                    if (("category" in object and object["category"] == category) and "isTroc" in object and object["isTroc"] == True) or ((
                            "ville" in object and object["ville"] == ville) and "isTroc" in object and object["isTroc"] == True):
                        objectList.append(object)

        print(objectList)
    return objectList

def searchOneObject(imagename: str=""):
    """ For research """
    objectList = []

    for document in collection.find():
        if not document["objects"]:
            continue
        else:
            for object in document["objects"]:
                if ("imageName" in object and object["imageName"] == imagename):
                    objectList.append(object)

    print(objectList)
    return objectList

def objectOwner(imagename: str=""):
    """ For research """
    objectList = []
    firstname=""
    lastname=""
    email=""
    for document in collection.find():
        if document["first_name"]:
            firstname = document["first_name"]
        if document["last_name"]:
            lastname = document["last_name"]
        if document["email"]:
            email = document["email"]

        if not document["objects"]:
            continue
        else:
            for object in document["objects"]:
                if ("imageName" in object and object["imageName"] == imagename):
                    objectList.append(email)
                    objectList.append(firstname)
                    objectList.append(lastname)


    print(objectList)
    return objectList


def addProposal(name, description, value, category, imageName, ville, isTroc, connectedUserEmail, trocob):
    contextObjectId = "fake1d"
    # isTrue:bool=False
    conditionObjet = {
        "email": connectedUserEmail
    }

    for document in collection.find(conditionObjet):
        objectList = document["objects"]
        objectList.append({
            "name": name,
            "category": category,
            "value": value,
            "ville": ville,
            "description": description,
            "isTroc": isTroc,
            "imageName": imageName,
            "trocObjectImage": trocob
        })

        collection.update_one(conditionObjet, {"$set":
            {
                "objects": objectList
            }
        })

    for x in collection.find(conditionObjet):
        print(x)

    return None

def searchIsTrocObjectforclient(useremail) -> list:
    """ For research """
    objectList = []
    myquery = {"email": useremail}

    for document in collection.find(myquery):
        if not document["objects"]:
            continue
        else:
            for object in document["objects"]:
                if ("isTroc" in object and object["isTroc"] == True):
                    objectList.append(object)

        print(objectList)
    return objectList
def searchIsPropObjectforclient(useremail) -> list:
    """ For research """
    objectList = []
    myquery = {"email": useremail}

    for document in collection.find(myquery):
        if not document["objects"]:
            continue
        else:
            for object in document["objects"]:
                if ("isTroc" in object and object["isTroc"] == False):
                    objectList.append(object)

        print(objectList)
    return objectList

def proposalsForATroc(trocImage):
    """ For research """
    objectList = []

    for document in collection.find():
        if not document["objects"]:
            continue
        else:
            for object in document["objects"]:
                if (("isTroc" in object and object["isTroc"] == False) and ("trocob" in object and object["trocob"] == trocImage)):
                    objectList.append(object)

    print(objectList)
    return objectList
