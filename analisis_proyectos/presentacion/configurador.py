import os
directorio_base = os.path.abspath(os.path.dirname(__file__))


class Configurador:
    SECRET_KEY = os.urandom(32)
    WTF_CSRF_SECRET_KEY = "a csrf secret key"
    SQLACHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(directorio_base, 'proyecto.sqlite')

    @staticmethod
    def inicializar_app(app):
        pass
