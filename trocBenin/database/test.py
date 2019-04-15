import pymongo
import json
#from flask import Flask, render_template, url_for, request, session, redirect, jsonify

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["trocdb"]

clientCol = mydb["users"]

#myquery = {"message": []}


mydoc = clientCol.find()

for x in mydoc:
  print(x)

cursor = clientCol.find({})
file = open("collection.json", "w")
file.write('[')
for document in cursor:
  document.pop('_id')
  file.write(json.dumps(document))
  file.write(',')
file.write(']')

#This checks if a use exist

#client = MongoClient()
#db = myclient["trocdb"]
#collection = db.collection_name
