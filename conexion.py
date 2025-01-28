import mysql.connector
import os
#OS se encarga de estabalecer conexion con las variables de entorno 
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

connection = mysql.connector.connect(
    host=os.getenv('DB_HOST'),        # Dirección del servidor MySQL
    user=os.getenv('DB_USER'),        # Usuario de la base de datos
    password=os.getenv('DB_PASSWORD'), # Contraseña de la base de datos
    database=os.getenv('DB_NAME')     # Nombre de la base de datos
)

if connection.is_connected():
    print('Conexión exitosa a la base de datos')
else:
    print('Error de conexión')

# Cerrar la conexión
connection.close()
