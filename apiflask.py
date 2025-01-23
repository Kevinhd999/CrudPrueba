from flask import Flask

app = Flask(__name__)

@app.route('/', methods = ['GET'])

def hola_mundo():
    return "Hola mundo"

if __name__ == '__main__':
    app.run(port = 3000)