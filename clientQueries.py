


import pymongo
#from flask import Flask, render_template, url_for, request, session, redirect, jsonify

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["TrocBenin"]

clientCol = mydb["client"]

#This checks if a use exist


def loginUser(email, password):
    myquery = {"email": email, "password": password}
    #print(myquery)

    mydoc = clientCol.find(myquery)
    #mydb.system.indexes.find()
    counter = 0
    for x in mydoc:
        first_name = x['first_name']
        client_Id = str(x['_id'])
        counter = counter + 1

    clientDetails ={"first_name": "", "client_Id": ""}
    if(counter == 1):
        #print("My first name is: "+ first_name + " and my id is: "+client_Id)
        clientDetails = {"first_name":first_name, "client_Id":client_Id}

    return clientDetails
def userExist(email):
    myquery = {"email": email}
    mydoc = clientCol.find(myquery)
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

    x = clientCol.insert_one(mydict)
    return True


#dataC = loginUser("wpulver0@pen.io","oewafe")
#print("username is: " + dataC['first_name'] + " and id is: " + dataC['client_Id'])