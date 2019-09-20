"""
Servicio de Aplicacion que gestiona el tratamiento de los elementos o partes que constituyen el
componente se software a construir
"""
from sqlalchemy.orm import sessionmaker
from analisis_proyectos.dominio.entidades.elemento import *


class GestorElemento:
    """
    Clase de aplicación que es la responsable de realizar la
    administración de agregado Elemento compuesto de la entidad
    Elemento, y los objeto valor: dimension, esfuerzo y defecto
    Basicamente maneja los CRUD del agregado, no tiene otra
    responsabilidad
    """
    def __init__(self):
        self._elemento = None
        self._repositorio = None
        self._nuevo = False
        return

    def crear_elemento(self, nombre_elemento,
                             tipo_elemento,
                             descripcion,
                             id_componente):
        """
        Metodo Factoria que crea solo una nueva entidad elemento
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
        """
        Persiste los cambios en el agregado:
        Ya sea un elemento nuevo, se modifica los datos del elemento
        o se cambian los OV
        :return:
        """
        self._abrir_unidad_de_trabajo()
        if self._nuevo:
            try:
                if not self.existe_elemento(str(self._elemento.nombre_elemento)):
                    self._repositorio.agregar(self._elemento)
                else:
                    raise("Ya existe es elemento con el nombre:" + str(self._elemento.nombre_elemento))
            except Exception():
                print('Error al guardar')
        else:
            try:
                self._repositorio.actualizar(self._elemento)
            except Exception():
                print('Error al guardar')
        self._nuevo = False

        self._guarda_dimension()
        self._guarda_esfuerzo()
        self._guarda_defecto()

        self._cerrar_unidad_de_trabajo()
        return

    def _guarda_dimension(self):

        dimensiones = self._elemento.lista_dimensiones
        for item in dimensiones:
            if item[1] == "NUEVO":
                # llama al repositorio de dimensiones y guarda
                print("agrega")
                self._repositorio.agregar_dimension_elemento(item[0])
            elif item[1] == "CAMBIO":
                # llama al repositorio de dimensiones y actualiza
                print("actualiza")
            elif item[1] == "BORRADO":
                # llama al repositorio de dimensiones y elimina
                print("elimina")
        return

    def _guarda_esfuerzo(self):

        esfuerzos = self._elemento.lista_esfuerzos
        for item in esfuerzos:
            if item[1] == "NUEVO":
                # llama al repositorio de dimensiones y guarda
                print("agrega")
                self._repositorio.agregar_esfuerzo_elemento(item[0])
            elif item[1] == "CAMBIO":
                # llama al repositorio de dimensiones y actualiza
                print("actualiza")
            elif item[1] == "BORRADO":
                # llama al repositorio de dimensiones y elimina
                print("elimina")
        return

    def _guarda_defecto(self):

        defectos = self._elemento.lista_defectos
        for item in defectos:
            if item[1] == "NUEVO":
                # llama al repositorio de dimensiones y guarda
                print("agrega")
                self._repositorio.agregar_defecto_elemento(item[0])
            elif item[1] == "CAMBIO":
                # llama al repositorio de dimensiones y actualiza
                print("actualiza")
            elif item[1] == "BORRADO":
                # llama al repositorio de dimensiones y elimina
                print("elimina")
        return

    def recuperar_elemento_por_nombre(self, nombre):
        self._abrir_unidad_de_trabajo()
        self._elemento = self._repositorio.recuperar_por_nombre(nombre)
        for dim in self._repositorio.recuperar_dimensiones(self._elemento.identificacion):
            self._elemento.agregar_dimension(dim)
        self._cerrar_unidad_de_trabajo()
        return self._elemento

    def recuperar_elemento(self, id_elemento):
        self._abrir_unidad_de_trabajo()
        self._elemento = self._repositorio.recuperar(id_elemento)
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
        return

    def sacar_dimension(self, dimension):
        self._elemento.eliminar_dimension(dimension)
        return

    def cambiar_dimension(self, dimension):
        self._elemento.modificar_dimension(dimension)
        return

    def recuperar_dimensiones(self):
        for item in self._repositorio.recuperar_dimensiones(self._elemento.identificacion):
            print(item)
        return

    def registrar_esfuerzo(self, actividad, esfuerzo):
        esf = Esfuerzo(actividad, esfuerzo, self._elemento.identificacion)
        self._elemento.agregar_esfuerzo(esf)
        return

    def eliminar_registro_de_esfuerzo(self, esfuerzo):
        pass

    def cambiar_registro_de_esfuerzo(self, esfuerzo):
        pass

    def recuperar_registro_de_esfuerzos(self):
        pass

    def registrar_defecto(self, fase, cantidad):
        defec = Defecto(fase, cantidad, self._elemento.identificacion)
        self._elemento.agregar_defecto(defec)
        return

    def elminar_registro_de_defecto(self, defecto):
        pass

    def cambiar_registro_de_defecto(self, defecto):
        pass

    def recuperar_registro_de_defectos(self):
        pass

    def _abrir_unidad_de_trabajo(self):
        sesion = sessionmaker(bind=self._repositorio.contexto.recurso)
        self._repositorio.contexto.sesion = sesion()
        return

    def _cerrar_unidad_de_trabajo(self):
        self._repositorio.contexto.sesion.commit()
        return
