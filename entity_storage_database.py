#this file is mongodb entity storage database file , which is storing entities which we are getting from client side
#(android app)

import dummy_data
from pymongo import MongoClient

data_base={}
sent=[]

client = MongoClient()
client = MongoClient('mongodb://localhost:27017/')
db = client.test_database
db = client['entity_storage_db']
entities = db.entities



