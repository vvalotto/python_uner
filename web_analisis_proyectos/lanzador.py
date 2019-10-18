from flask import Flask, request, redirect, url_for
import requests
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask import render_template
from analisis_proyectos.app.forms import *
from analisis_proyectos.app.models import *
from analisis_proyectos.app.configurador import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
bootstrap = Bootstrap(app)
moment = Moment(app)
URL_app_api = 'http://localhost:5050/'

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/proyectos/")
def proyecto_lista():
    formulario = ListaProyectoForm()
    formulario.inicializar()

    url_proyecto = URL_app_api + 'proyectos/'
    respuesta = requests.get(url_proyecto).json()

    for item in respuesta:
        formulario.lista_proyectos.append(item)
        
    return render_template("proyectos.html", form=formulario)


@app.route("/componentes/")
def componente_lista():
    return render_template("componentes.html")


@app.route("/elementos/")
def elementos_lista():
    return render_template("elementos.html")

@app.route("/proyecto/", methods=["POST"])
@app.route("/proyecto/<string:id>", methods=["GET", "POST"])
def proyecto(id):
    formulario = ProyectoForm()
    formulario.inicializar()
    proyecto = ProyectoVM(config.gestor_proyecto)

    if id != "0": #Hay proyecto identificado
        if request.method == "GET":
            if proyecto.recuperar_proyecto(id) is None:
                return redirect(url_for("index"))
            else:
                proyecto.listar_modulos()
                formulario.id = proyecto.identificador
                formulario.nombre_proyecto = proyecto.nombre
                formulario.descripcion = proyecto.descripcion
                formulario.tipo_proyecto = proyecto.tipo
                formulario.fecha_fin = proyecto.fecha_fin

                for item in proyecto.lista:
                    formulario.lista_modulos.append(item)
    else:
        if request.method == "POST":
            nombre_proyecto = request.form.get("nombre_proyecto")
            tipo_proyecto = request.form.get("tipo_proyecto")
            descripcion = request.form.get("descripcion")
            fecha_fin = request.form.get("fecha_fin")
            proyecto.agregar_proyecto(nombre_proyecto, tipo_proyecto, descripcion, fecha_fin)
            return redirect("/proyectos/")
        else:
            formulario.id = id

    return render_template("proyecto.html", form=formulario)


@app.route("/componente/", methods=["POST"])
@app.route("/componente/<string:id>/", methods=["GET", "POST"])
def componente(id):
    formulario = ComponenteForm()
    formulario.inicializar()
    componente = ComponenteVM(config.gestor_componente)

    if id != 0:
        resultado = componente.recuperar_componente(id)
        if resultado is None:
            return redirect(url_for("index"))
        else:
            componente.listar_elementos()
            formulario.nombre_componente = componente.nombre
            formulario.tipo_componente = componente.tipo
            formulario.id = componente.identificador
            formulario.proyecto = componente.proyecto
            for item in componente.lista_elementos:
                formulario.lista_elementos.append(item)
    return render_template("componente.html", form=formulario)


@app.route("/elemento/", methods=["POST"])
@app.route("/elemento/<string:id>/", methods=["GET", "POST"])
def elemento(id):
    formulario = ElementoForm()
    formulario.inicializar()
    elemento = ElementoVM(config.gestor_elemento)

    resultado = elemento.recuperar_elemento(id)
    if id != 0:
        if resultado is None:
            return redirect(url_for("index"))
        else:
            elemento.recuperar_elemento(id)
            formulario.nombre_elemento = elemento.nombre_elemento
            formulario.tipo_elemento = elemento.tipo_elemento
            formulario.id = elemento.identificador
            formulario.descripcion = elemento.descripcion

            for item in elemento.dimensiones:
                formulario.dimensiones.append(item[0])

            for item in elemento.esfuerzos:
                formulario.esfuerzos.append(item[0])

            for item in elemento.defectos:
                formulario.defectos.append(item[0])

            formulario.componente = elemento.componente
            formulario.proyecto = elemento.proyecto

    return render_template("elemento.html", form=formulario)


if __name__ == '__main__':
    config = Configurador
    app.run(debug=True)