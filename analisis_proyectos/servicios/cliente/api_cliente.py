from flask import  Flask, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/prueba/')
def prueba():
    url = 'http://localhost:5050/proyectos/'
    resultado = requests.get(url)
    res = resultado.json()
    for item in res:
        descripcion = item['descripcion']
        nombre = item['nombre_proyecto']
    return descripcion + '- ' + nombre

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)