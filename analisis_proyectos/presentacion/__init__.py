from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from .configurador import Configurador

bootstrap = Bootstrap()
moment = Moment()


def crear_app():
    app = Flask(__name__)
    config = Configurador()
    app.config.from_object(configurador)
    config.inicializar_app(app)

    bootstrap.init_app(app)
    moment.init_app(app)

    from .webapp.principal import principal as principal_blueprint
    app.register_blueprint(principal_blueprint)

    return app
