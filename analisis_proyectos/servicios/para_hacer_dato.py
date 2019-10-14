from flask import Flask, request
from flask_restful import Resource, Api
from flask_restful import fields, marshal_with

app = Flask(__name__)
api = Api(app)
para_hacer = {}

campos = {
    'tarea': fields.String,
    'uri': fields.Url('todo_ep')
}


class ParaHacerDato():

    def __init__(self, para_hacer_id, tarea):
        self._para_hacer_id = para_hacer_id
        self._tarea = tarea


class ParaHacer(Resource):
    @marshal_with(campos)
    def get(self, **kwargs):
        return ParaHacerDato(para_hacer_id='mi_todo', tarea='Comprar la leche')


class ParaHacerSimple(Resource):

    def get(self, para_hacer_id):
        return {para_hacer_id: para_hacer[para_hacer_id]}

    def put(self, para_hacer_id):
        para_hacer[para_hacer_id] = request.form['data']
        return {para_hacer_id: para_hacer[para_hacer_id]}


api.add_resource(ParaHacerSimple, '/<string:para_hacer_id>')
api.add_resource(ParaHacer, '/para_hacer/')

if __name__ == '__main__':
    app.run(debug=True)