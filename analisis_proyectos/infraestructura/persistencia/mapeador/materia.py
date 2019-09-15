"""

"""
from sqlalchemy import MetaData

from estructura_academica.dominio.entidades.materia import *
from estructura_academica.infraestructura.persistencia.modelo.base_de_datos import *

class MapeadorDatosMateria:

    def __init__(self, contexto):
        self._contexto = contexto
        self._entidad = None
        self._dto_base_datos = None
        return

    def dto_a_entidad(self, dto):
        self._dto_base_datos = dto
        nombre_carrera = NombreMateria(self._dto_base_datos.nombre_carrera)
        codigo_carrera = Codigo(self._dto_base_datos.codigo_carrera)
        plan = self._dto_base_datos.plan
        id_materia = IdCarrera(self._dto_base_datos.id_carrera)
        self._entidad = Materia(codigo_carrera, nombre_carrera, plan, id_materia)
        self._entidad.identificacion = self._dto_base_datos.id
        return self._entidad

    def entidad_a_dto(self, materia):
        self._entidad = materia
        self._dto_base_datos = MateriaDTO()
        self._dto_base_datos.metadata = MetaData(bind=self._contexto.recurso)
        self._dto_base_datos.id = materia.identificacion
        self._dto_base_datos.codigo_carrera = materia.codigo_carrera.codigo
        self._dto_base_datos.nombre_carrera = materia.nombre_carrera.texto
        self._dto_base_datos.plan = materia.plan
        self._dto_base_datos.id_unidad_academica = materia.id_carrera
        return self._dto_base_datos
