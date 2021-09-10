#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pymongo
import pprint
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = "SZ4lYd7M5Unbl8i6HxuCAcHkk"
csecret = "GNw2axdBaXr69HC0nAUO6OIu8eDFSIjR8NRkAk6wfWEp9YEVdd"
atoken = "1631284146-RVFxn5bXKbv5hzaLSLnYH0FTJC58qn7Bu9nRFEY"
asecret = "3fEyfLMJWWjja8beca5aZO1wHrXCVIbVwCaB4Irisr5SG"
#####################################


class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = mycol.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())



'MONGODB'
myclient = pymongo.MongoClient("mongodb://localhost:27017")  
try:
    mydb=myclient["pulso_politico"]
    mycol=mydb["candidatos-info"]
except:
    mydb=myclient["pulso_politico"]
    mycol=mydb["candidatos-info"]



twitterStream.filter(track=['Elecciones Ecuador','Pulso Politico Ecuador','Elecciones Ecuador 2021','Lasso','Arauz','Yaku','Guillermo Lasso presidente'])


# In[ ]:




