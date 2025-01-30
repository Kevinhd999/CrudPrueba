import time
import schedule
import sys
import os

# Agregar el directorio raíz al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from dbetl.model.db_manager import validate_and_update_tables

def main():
    # Aquí va el código principal que deseas ejecutar periódicamente
    print("Ejecutando tarea principal...")

def ejecutar_con_tiempo():
    validate_and_update_tables()
    main()
    schedule.every(10).minutes.do(main)

if __name__ == "__main__":
    ejecutar_con_tiempo()
    while True:
        schedule.run_pending()
        time.sleep(1)