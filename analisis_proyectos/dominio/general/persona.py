"""
--------------------------
Proyecto = ddd-evaluaciones
Modulo = persona
Autor = admin
Fecha creación = 23/10/16
--------------------------
"""
from .nombre import *

class Persona:

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @nombre
    def nombre(self, valor):
        self._nombre = valor
        return

    @property
    def ubicacion(self):
        return self._ubicacion

    @ubicacion
    def ubicacion(self, valor):
        self._ubicacion = valor
        return

    @property
    def informacion_contacto(self):
        return self._informacion_contacto

    @informacion_contacto
    def informacion_contacto(self, valor):
        self._informacion_contacto = valor
        return

    def __init__(self, identificacion,
                       nombre,
                       ubicacion='Sin Ubicacion',
                       informacion_contacto = 'Sin Información'):
        self._id = identificacion
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._informacion_contacto = informacion_contacto
        return

