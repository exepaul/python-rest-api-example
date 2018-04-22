#this is main server file which will start a server on port 5002 and then we can simply use ngrok to make it
#online , this have two request one is for retrieve data and second is receiving json data from client side


import json

from flask import Flask, url_for

import entity_storage_database


import json

app = Flask(__name__)

from flask import request

import data_base



#welcome message
@app.route('/')
def api_root():
    return 'Data_Labelling '




#retrieve request
#sending one random sentence

@app.route('/retrieve')
def api_articles():
    

    return data_base.random_sentence()



# receiving json request
#saving client data , (sentence , entities )


@app.route('/save', methods = ['POST'])
def postJsonHandler():
    print (request.is_json)
    content = request.get_json()
    for key,value in content.items():
        entity_storage_database.entities.insert({key:value})

    return 'JSON posted'


#starting the server on port 5002


if __name__ == '__main__':
    app.run(port=5002)
