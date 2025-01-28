from conexion import db_connection

def crear_usuario(cedula, nombre, edad):
    connection = db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO usuarios (cedula, nombre, edad) VALUES (%s, %s, %s)", (cedula, nombre, edad))
    connection.commit()# Confirma el movimiento o la transacción
    cursor.close()
    connection.close()

def lista_usuarios():
    connection = db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()# Devuelve todos los usuarios 
    cursor.close()
    connection.close()
    return usuarios

def usuario_por_cedula(cedula):
    connection = db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE cedula = %s", (cedula,))
    usuario = cursor.fetchone()# Devuelve un solo usuario si lo encuentra
    cursor.close()
    connection.close()
    return usuario

def actualizar_usuario(cedula, nombre, edad):
    connection = db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE usuarios SET nombre = %s, edad = %s WHERE cedula = %s", (nombre, edad, cedula))
    connection.commit() # Confirma el movimiento o la transacción
    cursor.close()
    connection.close()

def eliminar_usuario(cedula):
    connection = db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM usuarios WHERE cedula = %s", (cedula,))
    connection.commit()# Confirma el movimiento o la transacción
    cursor.close()
    connection.close()