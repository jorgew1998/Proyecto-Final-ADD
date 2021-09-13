#!/usr/bin/env python
# coding: utf-8

# In[5]:




from couchdbkit import Server, Database
from couchdbkit.loaders import FileSystemDocsLoader
from csv import DictReader
import sys, subprocess, math, os



def parseDoc(doc):
    for k,v in doc.items():
        if (isinstance(v,str)):
            #print k, v, v.isdigit()
            # #see if this string is really an int or a float
            if v.isdigit()==True: #int
                doc[k] = int(v)
            else: #try a float
                try:
                    if math.isnan(float(v))==False:
                        doc[k] = float(v) 
                except:
                    pass            
    return doc


def upload(db, docs):
    db.bulk_save(docs)
    del docs
    return list()


def uploadFile(fname, uri, dbname):


  #print 'Upload contents of %s to %s/%s' % (fname, uri, dbname)

  # #connect to the db
  theServer = Server(uri)
  db = theServer.get_or_create_db(dbname)

  #loop on file for upload
  reader = DictReader(open(fname, 'rU'), dialect = 'excel')  #see the python csv module 
         #for other options, such as using the tab delimeter. The first line in your csv 
         #file should contain all of the "key" and all subsequent lines hold the values 
         #for those keys.

  #used for bulk uploading
  docs = list()
  checkpoint = 100

  for doc in reader:
    newdoc = parseDoc(doc) #this just converts strings that are really numbers into ints and floats

    #Here I check to see if the doc is already on the database. If it is, then I assign
    #the _rev key so that it updates the doc on the db.

    if db.doc_exist(newdoc.get('_id')):
      newdoc['_rev'] = db.get_rev(newdoc.get('_id'))

    docs.append(newdoc)

    if len(docs)%checkpoint==0:
      docs = upload(db,docs)

  #don't forget the last batch        
  docs = upload(db,docs)



if __name__=='__main__':
  filename = 'pulsoxprovincias'
  uri = 'http:admin:admin@localhost:5984/'
  dbname = 'pulso_politico_provincias'

  uploadFile(filename, uri, dbname)


# In[4]:


pip install couchdbkit


# In[ ]:




