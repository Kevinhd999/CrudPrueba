import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()
Base = declarative_base()

DATABASE_URL = (
    f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)
engine = create_engine(DATABASE_URL)

class infoKids(Base):
    __tablename__ = 'info_kids'

    cedula = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String(50), nullable=False)
    años = Column(Integer, nullable=False)

def validate_and_update_tables():
    inspector = inspect(engine)

    # Validar y crear la tabla 'info_kids'
    if 'info_kids' not in inspector.get_table_names():
        print("Creando tabla 'info_kids'...")
        infoKids.__table__.create(engine)

Session = sessionmaker(bind=engine)
session = Session()
# Llamar a la función para validar y actualizar las tablas