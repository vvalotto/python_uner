from flask import Flask, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask import render_template
from analisis_proyectos.app.forms import ProyectoForm, ComponenteForm, ListaProyectoForm
from analisis_proyectos.app.models import *
from analisis_proyectos.app.configurador import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
bootstrap = Bootstrap(app)
moment = Moment(app)

posts = []

@app.route("/")
def index():
    return render_template("index.html", posts=posts)


@app.route("/proyecto/<string:nombre>", methods=["GET", "POST"])
def proyecto(nombre):
    formulario = ProyectoForm()
    formulario.inicializar()
    proyecto = ProyectoVM(config.gestor_proyecto)
    if request.method == "GET":
        if not proyecto.existe_proyecto(nombre):
            return redirect(url_for("index"))
        else:
            proyecto.obtener_proyecto(nombre)
            proyecto.listar_modulos()
            formulario.id = proyecto.identificador
            formulario.nombre_proyecto = nombre
            formulario.descripcion = proyecto.descripcion
            formulario.tipo_proyecto = proyecto.tipo

            for item in proyecto.lista:
                formulario.lista_modulos.append(item)

    return render_template("proyecto.html", form=formulario)


@app.route("/proyecto/lista/")
def proyecto_lista():
    form = ListaProyectoForm()
    form.inicializar()
    lista_proyectos = ListaProyectoVM(config.gestor_proyecto)
    lista_proyectos.obtener_proyectos()
    for item in lista_proyectos.obtener_proyectos():
        form.lista_proyectos.append(item)
    return render_template("proyecto_lista.html", form=form)


@app.route("/componente/", methods=['GET'], defaults={'nombre': None})
@app.route("/componente/<string:nombre>/")
def componente(nombre):
    form = ComponenteForm()
    form.inicializar()
    componente = ComponenteVM(config.gestor_componente)
    if nombre is not None:
        if not componente.existe_componente(nombre):
            return redirect(url_for("index"))
        else:
            componente.obtener_componente(nombre)
            componente.listar_elementos()
            form.nombre_componente = componente.nombre
            form.tipo = componente.tipo
            for item in componente.lista_elementos:
                form.lista_elementos.append(item)
    return render_template("componente.html", form=form)


@app.route("/elemento/")
def elemento():
    return render_template("elemento.html")


@app.route("/proyecto/<proy_id>", methods=["GET"])
def proy(comp_id):
    return


if __name__ == '__main__':
    config = Configurador
    app.run(debug=True)