######## Program Begins Here ########

#### Import Python libraries ####

import sqlite3
from google.cloud import storage 
import pandas as pd
import numpy as np
from datetime import datetime
import mysql.connector
import sys

#### Establish Connetion ####

cnx = mysql.connector.connect(user='postgres', password='Sujal@8422', host='34.31.153.206', 
                              database='testdb')

cursor = cnx.cursor()

#### Connetion Established ####

#### Execute query ####

query1 = ("select * from customer")
cursor.execute(query1)

#### Extremely Important: Close your SQL connection ####

cursor.close()
cnx.close()

######## Program Ends Here ########
