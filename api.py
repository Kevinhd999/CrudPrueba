from flask import Flask, request, abort, jsonify
from crud import crear_usuario, lista_usuarios, usuario_por_cedula, actualizar_usuario, eliminar_usuario

app = Flask(__name__)

@app.route('/')
def incial():
    return jsonify({"message": "Hola acabas de entrar a esta pagina"})

@app.route("/usuario", methods=['GET'])
def listar_usuarios():
    usuarios = lista_usuarios()
    if not usuarios:
        return '', 204  # No hay usuarios registrados
    else:
        return jsonify(usuarios), 200

@app.route('/registrar_usuario', methods=['POST'])
def registrar_dato():
    if request.json:
        cedula = request.json['cedula']
        nombre = request.json['nombre']
        edad = request.json['edad']
        if not (8 <= len(str(cedula)) <= 10):
            return jsonify({"mensaje": "La cédula debe tener entre 8 y 10 dígitos"}), 400
        if int(cedula) < 0:  
            return jsonify({"mensaje": "La cédula no puede ser negativa"}), 400
        if int(edad) < 0:
            return jsonify({"mensaje": "La edad no puede ser negativa"}), 400
        if int(edad) > 100:
            return jsonify({"mensaje": "La edad no puede ser verdad"}), 400


    if usuario_por_cedula(cedula):
        return jsonify({"mensaje": "La cédula ya está registrada"}), 409 # conflicto en la solicitud

    crear_usuario(cedula, nombre, edad)
    return jsonify({"mensaje": "Datos agregados correctamente"}), 201

@app.route('/editar_usuario/<int:cedula_id>', methods=['PUT'])
def editarusuario(cedula_id):
    if request.json:
        usuario = usuario_por_cedula(cedula_id)
        nombre = request.json.get('nombre', usuario[1]) 
        edad = request.json.get('edad', usuario[2])  
        if usuario is None:
            abort(404)
        if int(edad) < 0:
                return jsonify({"mensaje": "La edad no puede ser negativa"}), 400
        if int(edad) > 100:
                return jsonify({"mensaje": "La edad no puede ser verdad"}), 400
    

    actualizar_usuario(cedula_id, nombre, edad)
    return jsonify({"message": "Usuario actualizado", "data": {"cedula": cedula_id, "nombre": nombre, "edad": edad}}), 200

@app.route('/editar_key_usuario/<int:cedula_id>', methods=['PATCH'])
def actualizar_usuario_parcial(cedula_id):
    usuario = usuario_por_cedula(cedula_id)
    if usuario is None:
        abort(404)

    nombre = usuario[1]
    edad = usuario[2] 

    if 'nombre' in request.json:
        nombre = request.json['nombre']
    if 'edad' in request.json:
        edad = int(request.json['edad'])

    actualizar_usuario(cedula_id, nombre, edad)
    return jsonify({"mensaje": "Usuario actualizado parcialmente"}), 200

@app.route('/eliminar_usuario/<int:cedula_id>', methods=['DELETE'])
def eliminarusuario(cedula_id):
    usuario = usuario_por_cedula(cedula_id)
    if usuario is None:
        abort(404)
    eliminar_usuario(cedula_id)
    return jsonify({"message": "Usuario eliminado"}), 200

@app.errorhandler(404)
def error_endpoint(error):
    return f"Peticion no encontrada{error}", 404

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)