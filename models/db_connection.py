import sqlite3
#import psycopg2


async def db_consult(consulta):
    try:
        con = sqlite3.connect("db.db").cursor()
        return con.execute(consulta)
    except Exception as ex:
        print(ex)
        return -1
"""
async def db_connection():
    try:
        conenccion= await psycopg2.connect(
            host= '',
            user='',
            password='',
            database=''
        )
        print("coneccion exitosa")
        return conenccion
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
