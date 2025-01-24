from flask import Flask, request, make_response, redirect, abort

#flask es un micro framework, y markupsafe es una biblioteca de flask
#Make_response se encarga de cambiar el tipo de peticion
#Redirect se encarga de dirigir la nueva url 

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return "Hola acabas de entrar a esta pagina"

@app.route('/welcome')
def welcome():
    return 'Bienvenido, admin!'

@app.errorhandler(404)
def error_endpoint(error): #el parametro de error es de la funcion error_endpoint
    return f"Peticion no encontrada{error}", 404

@app.route('/usuario/<username>')
def perfil_usuruaio(username): #es un parametro de ruta, para poder asisgnar la variable 
    username = "Martin"
    return f"usuario {username}"

#@app.route('/ciclo')
#def index():
#    return redirect(url_for('/home'))

@app.route('/prohibido', methods = ['GET'])
def login():
    abort(401) #abort genera que se cierre la vista, lo que puede indicar que el usuario no tiene permisos para ingresar a esa url


@app.route("/home", methods = ['GET'])

def redireccion():
    user_ip_information = request.remote_addr # request.remote.addr detecta el ip del cliente que hace la solicitud 
    response = make_response(redirect("/redireccion")) #La manera de crear la nueva direccion y redirect lo dirige 
    response.set_cookie("user_ip_information", user_ip_information)#Almacena las cookies del cliente
    return response


@app.route("/redireccion", methods = ['GET'])
def informacion():
    user_ip = request.cookies.get("user_ip_information") #request.cookies.get solicita las cookies 
    return f"Su ip es {user_ip}" #retorna la varible user_ip 


#----------------------------------------------------------------------------------#
if __name__ == '__main__':
    app.run(port = 5000, host='0.0.0.0', debug = True)