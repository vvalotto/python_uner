import os
directorio_base = os.path.abspath(os.path.dirname(__file__))


class Configurador:
    CLAVE_SECRETA = os.environ.get('SECRET_KEY')
    SQLACHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(directorio_base, 'proyecto.sqlite')

    @staticmethod
    def inicializar_app(app):
        pass
