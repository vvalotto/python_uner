"""
Se implementa el repositorio de la Unidad Academica en Base de Datos
"""
from analisis_proyectos.dominio.entidades.base_repositorio_elemento import *
from analisis_proyectos.infraestructura.persistencia.modelo.base_de_datos_proyectos import *
from .DB_repositorio_dimension import *


class DBRepositorioElemento(BaseRepositorioElemento):

    def __init__(self, contexto, mapeador):
        super().__init__(contexto)
        self._mapeador = mapeador
        self._repo_dimension = DBRepositorioDimension()
        return

    def agregar(self, elemento):
        try:
            sesion = self.contexto.sesion
            c = self._mapeador.entidad_a_dto(elemento)
            sesion.add(c)
        except Exception("Error al guardar"):
            print("Repositorio de Elemento")
        return

    def actualizar(self, elemento):
        """
        Para actualizar la entidad persistida, se pasa la entidad modificada y:
            se mapea la entidad a la estructura de tabla
            se recupera la entidad existente por el id
            se copia la estructura mapeada a la recuperada
            se comitea
        :param componente:
        :return:
        """
        try:
            sesion = self.contexto.sesion
            elemento_modificado = self._mapeador.entidad_a_dto(elemento)
            elemento_recuperado = sesion.query(ComponenteDTO).get(elemento.identificacion)
            self._copiar_registro(elemento_modificado, elemento_recuperado)
        except Exception("Error al actualizar"):
            print("Repositorio de elemento")
        return

    def recuperar(self, identificacion):
        try:
            sesion = self.contexto.sesion
            elemento_dto = sesion.query(ElementoDTO).get(identificacion)
            componente = self._mapeador.dto_a_entidad(elemento_dto)
        except Exception("Error al recuperar"):
            componente = None
            print("Repositorio de Elemento")
        return componente

    def recuperar_por_nombre(self, nombre):
        try:
            sesion = self.contexto.sesion
            elemento_dto = sesion.query(ElementoDTO).\
                filter(ElementoDTO.nombre_elemento == nombre)[0]
            carrera = self._mapeador.dto_a_entidad(elemento_dto)
        except Exception("Error al recuperar"):
            carrera = None
            print("Repositorio de Unidad Academica")
        return carrera

    def validar_existencia(self, nombre):
        try:
            sesion = self.contexto.sesion
            if len(list(sesion.query(ElementoDTO).
                        filter(ElementoDTO.nombre_elemento == nombre))) > 0:
                return True
            else:
                return False
        except Exception("Error al recuperar"):
            print("Repositorio de Elemento")
            return False

    def obtener_todo(self):
        try:
            lista_elementos = []
            sesion = self.contexto.sesion
            for elemento_dto in sesion.query(ElementoDTO).all():
                elemento = self._mapeador.dto_a_entidad(elemento_dto)
                lista_elementos.append(elemento)
            return lista_elementos
        except Exception("Error al recuperar"):
            print("Repositorio de Elemento")
            return None

    def obtener_por_proyecto(self, proyecto):
        try:
            lista_elementos = []
            sesion = self.contexto.sesion
            for componente_dto in sesion.query(ComponenteDTO).filter_by(id_proyecto = proyecto):
                lista_elementos.append(self.obtener_por_componente(componente_dto.id))
            return lista_elementos
        except Exception("Error al recuperar"):
            print("Repositorio de Elemento")
            return None

    def obtener_por_componente(self, componente):
        try:
            lista_elementos = []
            sesion = self.contexto.sesion
            for elemento_dto in sesion.query(ElementoDTO).filter_by(id_componente = componente):
                elemento = self._mapeador.dto_a_entidad(elemento_dto)
                lista_elementos.append(elemento)
            return lista_elementos
        except Exception("Error al recuperar"):
            print("Repositorio de Elemento")
            return None

    def agregar_dimension_elemento(self, dimension_elemento):
        return

    def eliminar_dimension_elemento(self, dimension_elemento):
        return

    def recuperar_dimension_elemento(self, dimension_elemento):
        return

    def validar_existencia_dimension_elemento(self, dimension_elemento):
        return


    @staticmethod
    def _copiar_registro(desde, hacia):
        hacia.nombre_componente = desde.nombre_componente
        hacia.tipo_componente = desde.tipo_componente
        return
