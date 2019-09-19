"""
Servicio de Aplicacion que gestiona el tratamiento de las unidades academicas
"""
from sqlalchemy.orm import sessionmaker
from analisis_proyectos.dominio.entidades.elemento import *


class GestorElemento:
    """
    Clase de aplicación que es la responsable de realizar la
    administración de la entidad Componente.
    Basicamente maneja los CRUD de la entidad, no tiene otra
    responsabilidad
    """
    def __init__(self):
        self._elemento = None
        self._repositorio = None
        self._nuevo = False
        self._cambio_dimension = None
        return

    def crear_elemento(self, nombre_elemento,
                             tipo_elemento,
                             descripcion,
                             id_componente):
        """
        Metodo Factoria que crea una nueva entidad
        :return: la proyecto creado
        """
        self._elemento = Elemento(nombre_elemento, tipo_elemento, descripcion, id_componente)
        self._nuevo = True
        return self._elemento

    def asignar_repositorio(self, repositorio):
        """
        Asocia el repositorio donde se persisten las entidades
        :param repositorio:
        :return:
        """
        self._repositorio = repositorio
        return

    def guardar_elemento(self):
        self._abrir_unidad_de_trabajo()
        if self._nuevo:
            try:
                self._repositorio.agregar(self._elemento)
            except Exception():
                print('Error al guardar')
        else:
            try:
                self._repositorio.actualizar(self._elemento)
            except Exception():
                print('Error al guardar')
        self._nuevo = False

        if self._cambio_dimension == "NUEVO":
            # llama al repositorio de dimensiones y guarda
            a = 1
        elif self._cambio_dimension == "MODIFICADO":
            #l lama al repositorio de dimensiones y actualiza
            a = 1
        else:
            # llama al repositorio de dimensiones y elimina
            self._cerrar_unidad_de_trabajo()
        return

    def recuperar_elemento_por_nombre(self, nombre):
        self._abrir_unidad_de_trabajo()
        self._elemento = self._repositorio.recuperar_por_nombre(nombre)
        self._cerrar_unidad_de_trabajo()
        return self._elemento

    def recuperar_elemento(self, id_elemento):
        self._abrir_unidad_de_trabajo()
        self._elemento= self._repositorio.recuperar(id_elemento)
        self._cerrar_unidad_de_trabajo()
        return self._elemento

    def obtener_elementos_del_proyecto(self, proyecto):
        self._abrir_unidad_de_trabajo()
        lista_elementos = self._repositorio.obtener_por_proyecto(proyecto)
        self._cerrar_unidad_de_trabajo()
        return lista_elementos

    def obtener_elementos_del_componente(self, componente):
        self._abrir_unidad_de_trabajo()
        lista_elementos = self._repositorio.obtener_por_proyecto(componente)
        self._cerrar_unidad_de_trabajo()
        return lista_elementos

    def existe_elemento(self, nombre):
        self._abrir_unidad_de_trabajo()
        valida = self._repositorio.validar_existencia(nombre)
        self._cerrar_unidad_de_trabajo()
        return valida

    def dimensionar_elemento(self, dimension, valor):
        tipo_dim = TipoDimension(dimension)
        dim = Dimension(tipo_dim, valor, self._elemento.identificacion)
        self._elemento.agregar_dimension(dim)
        self._cambio_dimension = "NUEVO"
        return

    def sacar_dimension(self, dimension):
        return

    def _abrir_unidad_de_trabajo(self):
        sesion = sessionmaker(bind=self._repositorio.contexto.recurso)
        self._repositorio.contexto.sesion = sesion()
        return

    def _cerrar_unidad_de_trabajo(self):
        self._repositorio.contexto.sesion.commit()
        return
