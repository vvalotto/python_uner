from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
para_hacer = {}


class ParaHacerSimple(Resource):

    def get(self, para_hacer_id):
        return {para_hacer_id: para_hacer[para_hacer_id]}

    def put(self, para_hacer_id):
        para_hacer[para_hacer_id] = request.form['data']
        return {para_hacer_id: para_hacer[para_hacer_id]}


api.add_resource(ParaHacerSimple, '/<string:para_hacer_id>')

if __name__ == '__main__':
    app.run(debug=True)