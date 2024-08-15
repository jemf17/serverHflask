import sqlite3
#import psycopg2

def db_connection():
    return sqlite3.connect("H_M.db").cursor()

"""
async def db_connection():
    try:
        connection= await psycopg2.connect(
            host= '',
            user='',
            password='',
            database=''
        )
        print("coneccion exitosa")
        connection.set_session(autocommit=True)
        return connection
    except Exception as ex:
        print(ex)
        return -1

async def db_consult(consulta):
    try:
        db = await db_connection()
        cursor = db.cursor()
        return cursor.execute(consulta)
    except Exception as ex:
        print(ex)
        return -1
"""
