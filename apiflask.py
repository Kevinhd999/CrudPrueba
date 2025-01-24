from flask import Flask, request, make_response, redirect

app = Flask(__name__)

@app.route('/home', methods = ['GET'])

def hola_mundo():
    user_ip_information = request.remote_addr # request:remote.addr detecta el ip del cliente que hace la solicitud 
    response = make_response(redirect("/Redireccion")) 
    response = set.cookies ("user_ip_information", user_ip_information)
    return response


@app.route('/Redireccion')
def informacion():
    user_ip = request.cookies.get("user_ip_information")
    return f"Su ip es {user_ip}"

if __name__ == '__main__':
    app.run(port = 3000, debug = True)