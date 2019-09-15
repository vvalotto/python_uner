"""
Clase Abstracta que define el repositorio de la Unidad Academica
"""
from .base_repositorio import *


class BaseRepositorioComponente(BaseRepositorio):

    @abstractmethod
    def agregar(self, entidad):
        pass

    @abstractmethod
    def actualizar(self, entidad):
        pass

    @abstractmethod
    def recuperar(self, id):
        pass

    @abstractmethod
    def validar_existencia(self, criterio):
        pass

    @abstractmethod
    def recuperar_por_nombre(self, nombre):
        pass

    @abstractmethod
    def obtener_todo(self):
        pass
