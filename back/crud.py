from conexion import db_connection

# Función genérica para manejar la conexión y el cursor
def ejecutar_query(query, params=None, fetchone=False, fetchall=False):
    connection = db_connection()
    cursor = connection.cursor()

    cursor.execute(query, params or ())
    if fetchone:
        result = cursor.fetchone()  # fetchone() obtiene la primera fila de un conjunto de resultados
    elif fetchall:
        result = cursor.fetchall()  # fetchall() obtiene todas las filas de un conjunto de resultados
    else:
        result = None

    if query.strip().lower().startswith(('insert', 'update', 'delete')):  # strip() elimina los espacios en blanco al principio y al final de la cadena Y startswith() devuelve True si la cadena comienza con el valor especificado
        connection.commit()  # commit() guarda los cambios realizados en la base de datos
    cursor.close()
    connection.close()
    
    return result

def crear_usuario(cedula, nombre, edad):
    query = "INSERT INTO usuarios (cedula, nombre, edad) VALUES (%s, %s, %s)"
    ejecutar_query(query, (cedula, nombre, edad))

def lista_usuarios():
    query = "SELECT * FROM usuarios"
    return ejecutar_query(query, fetchall=True)

def usuario_por_cedula(cedula):
    query = "SELECT * FROM usuarios WHERE cedula = %s"
    return ejecutar_query(query, (cedula,), fetchone=True)

def actualizar_usuario(cedula, nombre, edad):
    query = "UPDATE usuarios SET nombre = %s, edad = %s WHERE cedula = %s"
    ejecutar_query(query, (nombre, edad, cedula))

def eliminar_usuario(cedula):
    query = "DELETE FROM usuarios WHERE cedula = %s"
    ejecutar_query(query, (cedula,))