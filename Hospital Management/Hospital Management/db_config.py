from pymongo import MongoClient
import mysql.connector

# MongoDB Connection
mongo_client = MongoClient('mongodb://localhost:27017/')
mongo_db = mongo_client['HospitalManagement']

# MySQL Connection
mysql_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345", 
    database="HospitalManagement"
)
mysql_cursor = mysql_db.cursor()
