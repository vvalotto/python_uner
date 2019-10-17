from flask import Flask, jsonify, abort, make_response, request, jsonify
from analisis_proyectos.servicios.configurador import *
import json

app_api = Flask(__name__)
config = Configurador

""" Errores """
@app_api.errorhandler(404)
def not_fount(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


""" Apis """
@app_api.route("/proyectos/", methods=["GET"])
def get_proyectos():
    """
    buscar los proyectos desde el gestor de proyectos
    :return:
    """
    lista_proyectos = []
    for proyecto in config.gestor_proyecto.obtener_todos_los_proyectos():
        p = {}
        p['nombre_proyecto'] = str(proyecto.nombre)
        p['tipo_proyecto'] = str(proyecto.tipo_proyecto)
        p['descripcion'] = str(proyecto.descripcion)
        lista_proyectos.append(p)

    return jsonify(lista_proyectos)


@app_api.route("/proyecto/<string:id>/", methods=["GET"])
def get_proyecto(id):
    """
    Recupera un proyecto o
    :param id:
    :return:
    """
    proyecto = config.gestor_proyecto.recuperar_proyecto(id)
    p = {}
    p['nombre_proyecto'] = str(proyecto.nombre)
    p['tipo_proyecto'] = str(proyecto.tipo_proyecto)
    p['descripcion'] = str(proyecto.descripcion)

    lista_componentes = []
    for componente in config.gestor_componente.obtener_componentes_del_proyecto(id):
        c={}
        c['nombre'] = str(componente.nombre)
        c['tipo_componente'] = str(componente.tipo_componente)
        c['identificacion'] = str(componente.identificacion)
        lista_componentes.append(c)

    p['lista_componentes'] = lista_componentes

    return jsonify(p)


@app_api.route("/proyecto/", methods=["POST"])
def post_proyecto():
    """
    Recupera un proyecto o
    :param id:
    :return:
    """
    datos = request.get_json()
    nombre_proyecto = datos['nombre_proyecto']
    tipo_proyecto = datos['tipo_proyecto']
    descripcion = datos['descripcion']
    fecha_fin = datos['fecha_fin']
    config.gestor_proyecto.crear_proyecto(nombre_proyecto, tipo_proyecto, descripcion, fecha_fin)
    config.gestor_proyecto.guardar_proyecto()
    return "Proyecto Guardado", 201


@app_api.route("/componentes/<string:id>/", methods=["GET"])
def get_componentes(id):
        return "Lista de componentes del proyecto"


@app_api.route("/componente/<string:id>", methods=["GET"])
def get_componente(id):
    return "Componente"


@app_api.route("/componente/", methods=["POST"])
def post_componente(id):
    return "OK"


@app_api.route("/elemento/<string:id>/", methods=["GET"])
def get_elementos(id):
        return "Lista de elementos del modulo"


@app_api.route("/elementol/<string:id>", methods=["GET"])
def get_elemento(id):
    return "Componente"


@app_api.route("/elemento/", methods=["POST"])
def postcomp_elemento(id):
    return "OK"

