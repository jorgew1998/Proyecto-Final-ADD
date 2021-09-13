#!/usr/bin/env python
# coding: utf-8

# In[6]:


import couchdb
import pymongo

server = couchdb.Server('http://admin:admin@localhost:5984/') 
couch_db = server['pulso_politico_provincias']

mongo_client = pymongo.MongoClient("mongodb+srv://usuario1:usuario1@cluster0.snkvt.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mongo_client_db = mongo_client.get_database('pulso_politico')

for row in couch_db.view('_all_docs', include_docs=True):
    print(row['doc'])
    if mongo_client_db.provincias.count_documents({"_id":row['doc']['_id']})==0:
        mongo_client_db.provincias.insert(row['doc'])


# In[ ]:




