from pymongo import MongoClient

client = MongoClient('localhost', 37017)
#Creating a db
db = client['summer-food']

#Creating collection
collection = db['icecreams']

#Data example

data_entry = {"brand": "turboIceCreams", "weight":25, "cost": 1.50}
data_forwards = {"brand": "turboIceCreams", "weight":25, "cost": 1.25, "nickname": "JZ"}
#Write a document to a collection

collection.insert_many([data_entry, data_forwards])