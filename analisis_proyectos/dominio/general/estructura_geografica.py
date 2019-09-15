"""
--------------------------
Proyecto = ddd-evaluaciones
Modulo = estructura_geografica
Autor = admin
Fecha creación = 23/10/16
--------------------------
"""

from .objeto_valor import *


class Region(ObjetoValor):
    @property
    def nombre(self):
        return self._nombre

    @property
    def tipo_region(self):
        return self._tipo_region

    def __init__(self, tipo_region, nombre):
        self._nombre = nombre
        self._tipo_region = tipo_region
        return

    def __str__(self):
        return self._tipo_region + ":" + self._nombre


class NodoGeografico:

    @property
    def region(self):
        return self._region

    @property
    def subregiones(self):
        return self._subregiones

    def __init__(self, region):
        self._region = region
        self._subregiones = []
        return

    def _agregar_subregion(self, subregion):
        self._subregiones.append(subregion)
        return

    def _tiene_subregion(self, subregion_buscada):
        for subregion in self._subregiones:
            if subregion == subregion_buscada:
                return True
        return False

    def __str__(self):
        return self._region.__str__()



class Pais(NodoGeografico):

    @property
    def provincias(self):
        return self.subregiones

    def agregar_provincia(self, provincia):
        self._agregar_subregion(provincia)
        return

    def tiene_provincia(self, nombre_provincia):
        provincia = Provincia(Region("Provincia", nombre_provincia))
        return self._tiene_subregion(provincia)


class Provincia(NodoGeografico):

    @property
    def departamentos(self):
        return self.subregiones

    def agregar_departamentos(self, departamento):
        self._agregar_subregion(departamento)
        return

    def tiene_departamente(self, departamento):
        self._tiene_subregion(departamento)


class Departamento(NodoGeografico):

    @property
    def cuidades(self):
        return self.subregiones

    def agregar_cuidades(self, ciudad):
        self._agregar_subregion(ciudad)
        return

    def tiene_ciudad(self, ciudad):
        self._tiene_subregion(ciudad)





class Nodo:

    @property
    def elemento(self):
        return self._elemento

    @property
    def nodo_padre(self):
        return self._nodo_padre

    def __init__(self, elemento):
        self._elemento = elemento
        self._nodo_padre = None
        self._nodos_hijos = []
        return

    def __str__(self):
        return self.elemento.__str__()

class ArbolJerarquico:

    def __init__(self, nodo_origen):
        self._nodo_origen = nodo_origen
        return

    def agregar_nodo(self, nodo, nodo_padre):
        n = self.buscar_nodo(nodo_padre)
        if n is not None:
            n._nodos_hijos.append(nodo)
        else:
            raise " No existe el nodo padre"

        return

    def buscar_nodo(self, nodo):
        if self._nodo_origen._elemento == nodo._elemento:
            return self._nodo_origen
        else:
            for nodo_hijo in self._nodo_origen._nodos_hijos:
                arbol = ArbolJerarquico(nodo_hijo)
                return arbol.buscar_nodo(nodo)








