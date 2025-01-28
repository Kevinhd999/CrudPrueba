import mysql.connector
import os
#OS se encarga de estabalecer conexion con las variables de entorno 
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

def db_connection():
    connection=  mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    return connection
