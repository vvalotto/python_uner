"""
Servicio de Aplicacion que gestiona el tratamiento de las materias
"""
from sqlalchemy.orm import sessionmaker

from estructura_academica.dominio.entidades.materia import *


class GestorCarrera:
    """
    Clase de aplicación que es la responsable de realizar la
    administración de la entidad Materia
    Basicamente maneja los CRUD de la entidad, no tiene otra
    responsabilidad
    """
    def __init__(self):
        self._materia = None
        self._repositorio = None
        self._nuevo = False
        return

    def crear_materia(self, codigo_materia,
                      nombre_materia,
                      plan,
                      id_carrera):
        self._materia = Materia(codigo_materia,
                      nombre_materia,
                      plan,
                      id_carrera)
        self._nuevo = True
        return self._materia

    def asignar_repositorio(self, repositorio):
        """
        Asocia el repositorio donde se persisten las entidades
        :param repositorio:
        :return:
        """
        self._repositorio = repositorio
        return

    def guardar_materia(self):
        self._abrir_unidad_de_trabajo()
        if self._nuevo:
            try:
                self._repositorio.agregar(self._materia)
            except Exception():
                print('Error al guardar')
        else:
            try:
                self._repositorio.actualizar(self._materia)
            except Exception():
                print('Error al guardar')
        self._cerrar_unidad_de_trabajo()
        self._nuevo = False
        return

    def recuperar_materia_por_nombre(self, nombre):
        self._abrir_unidad_de_trabajo()
        self._materia = self._repositorio.recuperar_por_nombre(nombre)
        self._cerrar_unidad_de_trabajo()
        return self._materia

    def recuperar_materia(self, id_materia):
        self._abrir_unidad_de_trabajo()
        self._materia = self._repositorio.recuperar(id_materia)
        self._cerrar_unidad_de_trabajo()
        return self._materia

    def obtener_todas_las_materias_por_carrera(self, id_unidad_academica):
        pass

    def existe_materia(self, nombre):
        self._abrir_unidad_de_trabajo()
        valida = self._repositorio.validar_exitencia(nombre)
        self._cerrar_unidad_de_trabajo()
        return valida

    def _abrir_unidad_de_trabajo(self):
        sesion = sessionmaker(bind=self._repositorio.contexto.recurso)
        self._repositorio.contexto.sesion = sesion()
        return

    def _cerrar_unidad_de_trabajo(self):
        self._repositorio.contexto.sesion.commit()
        return