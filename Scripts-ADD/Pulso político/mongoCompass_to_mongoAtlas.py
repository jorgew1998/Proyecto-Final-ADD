#!/usr/bin/env python
# coding: utf-8

# In[1]:



import json
from argparse import ArgumentParser
import requests
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId
import couchdb

try:
    client = MongoClient('localhost')
    print (client.list_database_names())
    clientatl = MongoClient('mongodb+srv://usuario1:usuario1@cluster0.snkvt.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    print (clientatl.list_database_names())
except requests.ConnectionError as e:
    raise e

#insert_many()
db = client['pulso_politico']
col = db['candidatos-info']
dbatl = clientatl['pulso_politico']
colatl = dbatl['ciudades']

for doc in col.find({}):
 print("saved")
 

for doc in col.find({}):
 colatl.insert_one(doc)
 print(doc)

for doc in colatl.find({}):
 print("saved")


# In[ ]:




