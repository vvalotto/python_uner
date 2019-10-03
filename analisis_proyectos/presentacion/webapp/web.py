from flask import Flask, make_response, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import Form

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/')
def index():
    return render_template('index.html', hora_actual=datetime.utcnow())


@app.route('/usuario/<nombre>')
def user(nombre):
    return render_template('user.html', nombre=nombre)


@app.errorhandler(404)
def pagina_no_encontrad(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def error_server(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(debug=True)
