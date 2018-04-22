import requests

import dummy_data

sent=[]

final_=[]
#sending_data

url=requests.get('http://127.0.0.1:5002/retrieve')

print("random_sentence {}".format(url.text))

# receiving json from client side

post_url=requests.post('http://127.0.0.1:5002/save',json=dummy_data.Entities)







