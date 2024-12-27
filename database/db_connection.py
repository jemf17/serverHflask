#import sqlite3
import os
import psycopg2
from dotenv import load_dotenv
from supabase import create_client
import boto3

class DBSingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class DB(metaclass=DBSingletonMeta):
    def db_connection(self):
        load_dotenv()
        try:
            connection=  psycopg2.connect(
                host= os.getenv('PG_HOST'),
                user=os.getenv('PG_USER'),
                password=os.getenv('PG_PASSWORD'),
                database=os.getenv('PG_BD')
            )
            connection.set_session(autocommit=True)
            return connection
        except Exception as ex:
            print("hay error", ex)
            return -1
    def supabase_connection(self):
        load_dotenv()

        url = os.getenv('LINK_SUPABASE')
        key = os.getenv('KEY_SUPABASE')

        return create_client(url, key)
    def s3_connection(self):
        try:
            load_dotenv()
            s3_client = boto3.client(
            "s3",
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
            aws_secret_access_key=os.getenv('AWS_SECRET_KEY'),
            region_name=os.getenv('S3_REGION_NAME'),)
            return s3_client
        except Exception as ex:
            print("Error en la conexion con S3", ex)
            return -1
