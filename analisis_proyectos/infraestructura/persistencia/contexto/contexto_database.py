"""
Definición del mecanismo de persistencia (Tecnología para almacenar los datos)
"""

from sqlalchemy import create_engine
from .contexto import *
from ..modelo.base_de_datos_proyectos import *


class ContextoDB(BaseContexto):
    """
    Implementa un contexto correspodiente a un motor de base de datos
    """

    @property
    def recurso(self):
        return self._recurso

    def __init__(self, recurso):
        """
        :param recurso:El recurso corresponde al nombre y motor de la base de datos
        :return:
        """
        super().__init__(recurso)
        self._recurso = create_engine(recurso)
        self._recurso.echo = True

    def inicializar_tablas(self):
        """
        Crear las tablas
        :return:
        """
        Base.metadata.bind = self._recurso
        Base.metadata.create_all()





