import hashlib
import csv

import csv
import random
from pymongo import MongoClient

data_base={}
sent=[]

client = MongoClient()
client = MongoClient('mongodb://localhost:27017/')
db = client.test_database
db = client['test3433_databse']
entities = db.entities
with open('data.csv','r') as f:

    reader=csv.reader(f)
    next(reader, None)

    for line in reader:


        id_uni = int(hashlib.md5(line[0].encode('utf-8')).hexdigest(), 16)


        db.entities.insert({str(id_uni):line[0]})




def get_record():
    return list(entities.find())

def random_sentence():
    random_sen=random.choice(list(entities.find_one().keys()))
    sent.append({random_sen:entities.find_one().get(random_sen)})
    db.entities.remove({random_sen:entities.find_one().get(random_sen)})

    return str(sent[-1])



