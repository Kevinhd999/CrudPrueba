import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Cargar las variables de entorno
load_dotenv()

# Definir la base para las clases de modelos
Base = declarative_base()

# Crear la URL de la base de datos
DATABASE_URL = (
    f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL)

# Definir la clase del modelo infoKids
class InfoKids(Base):
    __tablename__ = 'prueba'

    cedula = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String(50), nullable=False)
    años = Column(Integer, nullable=False)

# Función para validar y actualizar las tablas
def validate_and_update_tables():
    inspector = inspect(engine)

    # Validar y crear la tabla 'info_kids' si no existe
    if 'prueba' not in inspector.get_table_names():
        print("Creando tabla 'info_kids'...")
        InfoKids.__table__.create(engine)

# Crear una sesión de la base de datos
Session = sessionmaker(bind=engine)
session = Session()
# Llamar a la función para validar y actualizar las tablas