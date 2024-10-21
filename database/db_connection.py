#import sqlite3
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

'''
def db_connection():
    try:
        return sqlite3.connect("H_M.db")
    except Exception as ex:
        print(ex)
        return -1
'''



def db_connection():
    try:
        connection=  psycopg2.connect(
            host= os.getenv('PG_HOST'),
            user=os.getenv('PG_USER'),
            password=os.getenv('PG_PASSWORD'),
            database=os.getenv('PG_BD')
        )
        print("coneccion exitosa" )
        connection.set_session(autocommit=True)
        return connection
    except Exception as ex:
        print("hay error", ex)
        return -1
