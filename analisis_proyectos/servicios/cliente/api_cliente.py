from flask import  Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/prueba/')
def prueba():
    url = 'http://localhost:5000/todo/api/v1.0/tasks/2'
    resultado = requests.get(url)
    return resultado.json()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)