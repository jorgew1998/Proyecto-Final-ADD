from pymongo import MongoClient
import pandas as pd
import bson
from bson.raw_bson import RawBSONDocument
from pymongo.errors import ConnectionFailure
import sqlite3
recolectar = sqlite3.connect("BDHappiness.db")

dato1 = pd.read_csv('C:/Users/Usuario/Desktop/world-happiness-report-2021.csv', index_col=0)

dato1.to_sql('happiness_report', recolectar)




