"""
Clase Abstracta que define el repositorio
"""
from .base_repositorio import *


class BaseRepositorioEsfuerzo(BaseRepositorio):

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
    def recuperar_por_actividad(self, tipo):
        pass

    @abstractmethod
    def recuperar_por_elemento(self, elemento):
        pass

    @abstractmethod
    def obtener_todo(self):
        pass