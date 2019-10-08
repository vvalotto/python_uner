from flask import Flask, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask import render_template
from analisis_proyectos.app.forms import SignupForm, PostForm, ProyectoForm
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


@app.route("/admin/post/", methods=['GET', 'POST'], defaults={'post_id': None})
@app.route("/admin/post/<int:post_id>/", methods=['GET', 'POST'])
def post_form(post_id):
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        title_slug = form.title_slug.data
        content = form.content.data
        post = {'title': title, 'title_slug': title_slug, 'content': content}
        posts.append(post)
        return redirect(url_for('index'))
    return render_template("admin/post_form.html", form=form)


@app.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    form = SignupForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('index'))
    return render_template("signup_form.html", form=form)


@app.route("/proyecto/", methods=["GET", "POST"])
def proyecto():
    form = ProyectoForm()
    proyecto = ProyectoVM(config.gestor_proyecto)
    if form.validate_on_submit():
        if not proyecto.existe_proyecto(form.nombre_proyecto.data):
            return redirect(url_for("index"))
        else:
            proyecto.obtener_proyecto(form.nombre_proyecto.data)
            proyecto.listar_modulos()
            form.descripcion = proyecto.descripciom
            for item in proyecto.lista:
                form.lista_modulos.append(item)
    return render_template("proyecto.html", form=form)


@app.route("/componente/")
def componente():
    return render_template("componente.html")


@app.route("/elemento/")
def elemento():
    return render_template("elemento.html")


@app.route("/proyecto/<proy_id>", methods=["GET"])
def proy(comp_id):
    return


if __name__ == '__main__':
    config = Configurador
    app.run(debug=True)