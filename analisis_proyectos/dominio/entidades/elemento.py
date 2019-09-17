"""
Entidad Elemento
"""

from ..base.entidad import *
from ..base.texto_no_vacio import *

TIPO_ELEMENTO = ['Caso de Uso', 'Historia de Usuario', 'Escenario de Calidad', "Requerimiento", "POC"]
TIPO_ACTIVIDAD = ['Análsis', 'Diseño', 'Programación', 'Testing']
FASE_DEFECTO = ['TEST_FUNCIONAL', 'TEST_USUARIO', 'PRODUCCION']


class TipoDimension(TextoNoVacio):

    def __rep__(self):
        return self.texto


class Dimension(Entidad):

    @property
    def tipo_dimension(self):
        return self._tipo_dimension

    @tipo_dimension.setter
    def tipo_dimension(self, valor):
        self._nombre = valor
        return

    @property
    def valor_dimension(self):
        return self._valor_dimension

    @valor_dimension.setter
    def valor_dimension(self, valor):
        self._valor_dimension = valor
        return

    @property
    def identificacion_elemento(self):
        return self._id_elemento

    def __init__(self,  tipo_dimension, valor_dimension, elemento):
        super().__init__()
        self._tipo_dimension = tipo_dimension
        self._valor_dimension = valor_dimension
        self._id_elemento = elemento
        return

    def __repr__(self):
        return str(self.tipo_dimension) + ": " + str(self.valor_dimension)


class Esfuerzo(Entidad):

    @property
    def tipo_actividad(self):
        return self._tipo_actividad

    @tipo_actividad.setter
    def tipo_actividad(self, valor):
        if valor not in TIPO_ACTIVIDAD:
            raise("Error en el tipo de actividad")
        self._tipo_actividad = valor
        return

    @property
    def esfuerzo_actividad(self):
        return self._esfuerzo_actividad

    @esfuerzo_actividad.setter
    def esfuerzo_actividad(self, valor):
        self._esfuerzo_actividad = valor
        return

    @property
    def identificacion_elemento(self):
        return self._id_elemento

    def __init__(self, tipo_actividad, esfuerzo_actividad, elemento):
        super().__init__()
        if tipo_actividad not in TIPO_ACTIVIDAD:
            raise("Error en el tipo de actividad")
        self._tipo_actividad = tipo_actividad
        self._esfuerzo_actividad = esfuerzo_actividad
        self._id_elemento = elemento
        return

    def __repr__(self):
        return str(self.tipo_actividad) + ": " + str(self.esfuerzo_actividad)


class Defecto(Entidad):

    @property
    def fase_defecto(self):
        return self._fase_defecto

    @fase_defecto.setter
    def fase_defecto(self, valor):
        if valor not in FASE_DEFECTO:
            raise("Error en el tipo de fase")
        self._fase_defecto = valor
        return

    @property
    def cantidad_defecto(self):
        return self._cantidad_defecto

    @cantidad_defecto.setter
    def cantidad_defecto(self, valor):
        self._cantidad_defecto = valor
        return

    @property
    def identificacion_elemento(self):
        return self._id_elemento

    def __init__(self, fase_defecto, cantidad_defecto, elemento):
        super().__init__()
        if fase_defecto not in FASE_DEFECTO:
            raise("Error en el tipo de fase")
        self._fase_defecto = fase_defecto
        self._cantidad_defecto = cantidad_defecto
        self._id_elemento = elemento
        return

    def __repr__(self):
        return str(self.fase_defecto) + ": " + str(self.cantidad_defecto)


class NombreElemento(TextoNoVacio):

    def __rep__(self):
        return self.texto


class Elemento(Entidad):

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
        return

    @property
    def tipo_elemento(self):
        return self._tipo_elemento

    @tipo_elemento.setter
    def tipo_elemento(self, valor):
        if valor in TIPO_ELEMENTO:
            self._tipo_elemento = valor
        else:
            raise Exception("No es un tipo de elemento valido")
        return

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, valor):
        self._descripcion = valor
        return

    def __init__(self,  nombre, tipo_elemento, descripcion, componente):
        super().__init__()
        self._nombre = nombre
        if tipo_elemento in TIPO_ELEMENTO:
            self._tipo_elemento = tipo_elemento
        else:
            raise Exception("No es un tipo de elemnto valido")
        self._descripcion = descripcion
        self._id_componente = componente
        self._lista_dimensiones = []
        self._lista_esfuerzos = []
        self._lista_defectos = []
        return

    def agregar_dimension(self, dimension):

        return

    def agregar_esfuerzo(self, esfuerzo):
        return

    def agregar_defecto(self, defecto):
        return

    def __repr__(self):
        return str(self.nombre) + ": " + self._tipo_elemento

