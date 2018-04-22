#This file os opening the csv file , creating a unique md5 hash key for each sentence and

# storing the csv sentences to mongodb database and then there is a

#function random_sentence which is selecting a random sentence from mongodb database



import hashlib
import csv

import csv
import random
from pymongo import MongoClient

data_base={}
sent=[]


#creaiting database

client = MongoClient()
client = MongoClient('mongodb://localhost:27017/')
db = client.test_database
db = client['test3433_databse']
entities = db.entities


#reading_file
with open('data.csv','r') as f:

    reader=csv.reader(f)
    next(reader, None)

    for line in reader:


        #creating unique md5 hash for each string


        id_uni = int(hashlib.md5(line[0].encode('utf-8')).hexdigest(), 16)

        #storing in databse

        db.entities.insert({str(id_uni):line[0]})



#getting record function
def get_record():
    return list(entities.find())


#getting random sentence from database

def random_sentence():
    random_sen=random.choice(list(entities.find_one().keys()))
    if random_sen!='_id':
        sent.append({random_sen:entities.find_one().get(random_sen)})
        db.entities.remove({random_sen:entities.find_one().get(random_sen)})
        return str(sent[-1])
    else:
        return random_sentence()

