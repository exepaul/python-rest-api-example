import json

from flask import Flask, url_for

app = Flask(__name__)

from flask import request

import data_base


@app.route('/')
def api_root():
    return 'Data_Labelling '




@app.route('/retrieve')
def api_articles():
    

    return data_base.random_sentence()





@app.route('/save', methods = ['POST'])
def postJsonHandler():
    print (request.is_json)
    content = request.get_json()
    print (content)
    return 'JSON posted'




if __name__ == '__main__':
    app.run(port=5002)
