import os
from analisis_proyectos.presentacion import crear_app
# from analisis_proyectos.presentacion.webapp.modelos import
from flask_script import Manager


app = crear_app()
manager = Manager(app)

if __name__ == '__main__':
    app.run()