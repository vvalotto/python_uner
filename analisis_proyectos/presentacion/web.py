from flask import Flask, make_response, render_template
from flask_bootstrap import  Bootstrap
from analisis_proyectos.aplicacion.gestores.gestor_proyecto import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/usuario/<nombre>')
def user(nombre):
    return render_template('user.html', nombre=nombre)

if __name__ == "__main__":
    app.run(debug=True)