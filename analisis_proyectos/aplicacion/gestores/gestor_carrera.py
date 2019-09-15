"""
Servicio de Aplicacion que gestiona el tratamiento de las unidades academicas
"""
from sqlalchemy.orm import sessionmaker

from estructura_academica.dominio.entidades.carrera import *


class GestorCarrera:
    """
    Clase de aplicación que es la responsable de realizar la
    administración de la entidad Carrera
    Basicamente maneja los CRUD de la entidad, no tiene otra
    responsabilidad
    """
    def __init__(self):
        self._carrera = None
        self._repositorio = None
        self._nuevo = False
        return

    def crear_carrera(self, codigo_carrera,
                      nombre_carrera,
                      id_unidad_academica):
        self._carrera = Carrera(nombre_carrera,
                                codigo_carrera,
                                id_unidad_academica)
        self._nuevo = True
        return self._carrera

    def asignar_repositorio(self, repositorio):
        """
        Asocia el repositorio donde se persisten las entidades
        :param repositorio:
        :return:
        """
        self._repositorio = repositorio
        return

    def guardar_carrera(self):
        self._abrir_unidad_de_trabajo()
        if self._nuevo:
            try:
                self._repositorio.agregar(self._carrera)
            except Exception():
                print('Error al guardar')
        else:
            try:
                self._repositorio.actualizar(self._carrera)
            except Exception():
                print('Error al guardar')
        self._cerrar_unidad_de_trabajo()
        self._nuevo = False
        return

    def recuperar_carrera_por_nombre(self, nombre):
        self._abrir_unidad_de_trabajo()
        self._carrera = self._repositorio.recuperar_por_nombre(nombre)
        self._cerrar_unidad_de_trabajo()
        return self._carrera

    def recuperar_carrera(self, id_carrera):
        self._abrir_unidad_de_trabajo()
        self._carrera = self._repositorio.recuperar(id_carrera)
        self._cerrar_unidad_de_trabajo()
        return self._carrera

    def obtener_todas_las_carreras_por_ua(self, id_unidad_academica):
        pass

    def existe_carrera(self, nombre):
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