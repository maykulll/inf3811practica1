from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return ("BIENVENIDO A LA PRUEBA PARA CREAR FLASK CON PYTHON")
@app.route("/saludo")
def saludo():
    return ("Hola buenas tardes esta es una ruta donde se pueden crear otras vistas")
@app.route("/usuario")
def usuario():
    return ("Hola usuario")
@app.route("/sumas")
def sumas():
    return ("Esta es la ventana de sumas donde deberia estar todos los calculos matematicos")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
