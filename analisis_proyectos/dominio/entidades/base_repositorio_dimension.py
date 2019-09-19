"""
Clase Abstracta que define el repositorio de la Unidad Academica
"""
from .base_repositorio import *


class BaseRepositorioDimension(BaseRepositorio):

    @abstractmethod
    def agregar(self, ov):
        pass

    @abstractmethod
    def actualizar(self, ov):
        pass

    @abstractmethod
    def eliminar(self, ov):
        pass

    @abstractmethod
    def recuperar(self, ov):
        pass

    @abstractmethod
    def validar_existencia(self, ov):
        pass

    @abstractmethod
    def recuperar_por_tipo(self, tipo):
        pass

    @abstractmethod
    def recuperar_por_elemento(self, elemento):
        pass

    @abstractmethod
    def obtener_todo(self):
        pass
