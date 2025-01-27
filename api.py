from flask import Flask, request, make_response, redirect, abort, jsonify
#flask es un micro framework, y markupsafe es una biblioteca de flask
#Make_response se encarga de cambiar el tipo de peticion
#Redirect se encarga de dirigir la nueva url 
#jsonify se encarga de convertir los datos en formato json
#abort se encarga de cerrar la vista para autorizacion denegada 

datos = []

app = Flask(__name__)

@app.route('/')
def incial():
    return jsonify({"message": "Hola acabas de entrar a esta pagina"})


@app.route("/usuario", methods = ['GET'])
def usuarios():
    if datos == []:
        return jsonify({"message": "No hay usuarios registrados"}), 204
    else:
         return jsonify({"message": "Lista de usuarios", "data": datos})

@app.route('/añadir_usuario', methods=['POST'])
def anadir_dato():
        if not request.json or not 'cedula' in request.json or not 'nombre' in request.json or not 'edad' in request.json:
            #if not request.json se encarga que los datos respectivos sean enviados en formato json
            abort(400)  
        for usuario in datos:
            if usuario['cedula'] == int(request.json['cedula']):
                return jsonify({"mensaje": "La cedula ya esta registrada", "data": usuario}), 400
        nuevo_dato = {
            "cedula": int(request.json['cedula']),
            "nombre": request.json['nombre'],
            "edad": int(request.json['edad'])
        }
        datos.append(nuevo_dato)
        return jsonify({"mensaje": "Datos agregados correctamente", "data": nuevo_dato}), 201


@app.route('/editar_usuario/<int:cedula_id>', methods=['PUT'])
def editarusuario(cedula_id):
    usuario = next((usuario for usuario in datos if usuario['cedula'] == cedula_id), None)
    if usuario is None:
        abort(404)
    elif not request.json:
        abort(400)
    
    usuario['nombre'] = request.json.get('nombre', usuario['nombre'])
    usuario['edad'] = request.json.get('edad', usuario['edad'])
    
    return jsonify({"message": "Usuario actualizado", "data": usuario})

@app.route('/editar_key_usuario/<int:cedula_id>', methods=['PATCH'])
def actualizar_usuario_parcial(cedula_id):
    usuario = next((usuario for usuario in datos if usuario['cedula'] == cedula_id), None)
    if usuario is None:
        abort(404)
    if not request.json:
        abort(400)
    
    # Actualizar solo los campos proporcionados en la solicitud
    if 'nombre' in request.json:
        usuario['nombre'] = request.json['nombre']
    if 'edad' in request.json:
        usuario['edad'] = int(request.json['edad'])
    
    return jsonify({"mensaje": "Usuario actualizado parcialmente", "data": usuario})

@app.route('/eliminar_usuario/<int:cedula_id>', methods=['DELETE'])
def eliminarusuario(cedula_id):
    usuario = next((usuario for usuario in datos if usuario['cedula'] == cedula_id), None)
    if usuario is None:
        abort(404)
    datos.remove(usuario)
    return jsonify({"message": "Usuario eliminado", "data": datos})




@app.errorhandler(404)
def error_endpoint(error): #el parametro de error es de la funcion error_endpoint
    return f"Peticion no encontrada{error}", 404


#----------------------------------------------------------------------------------#
if __name__ == '__main__':
    app.run(port = 5000, host='0.0.0.0', debug = True)