from ..aplicacion.gestores.gestor_proyecto import *


class ProyectoVM:

    def __init__(self):
        self._gestor_proyecto = GestorProyecto()
        self._gestor_proyecto.asignar_repositorio()

class Proyecto:

    @property
    def nombre(self):
        return self._nombre

    @property
    def descripciom(self):
        return self._descripcion

    @property
    def lista(self):
        return self._modulos

    def __init__(self):
        self._nombre = "Mi proyecto"
        self._descripcion = "Descripcion"
        self._modulos = []
        return

    def existe_proyecto(self, nombre):
       if nombre == self._nombre:
           return True
       else:
           return False

    def listar_modulos(self):
        self._modulos.append("mod 1")
        self._modulos.append("mod 2")
        self._modulos.append("mod 3")
        return