from analisis_proyectos.dominio.entidades.base_repositorio_dimension import *
from analisis_proyectos.infraestructura.persistencia.modelo.base_de_datos_proyectos import *
import uuid


class DBRepositorioDimension(BaseRepositorioDimension):

    def __init__(self, contexto, mapeador):
        super().__init__(contexto)
        self._mapeador = mapeador
        return

    def agregar(self, dimension):
        try:
            sesion = self.contexto.sesion
            d = self._mapeador.entidad_a_dto(dimension)
            d.id = str(uuid.uuid4())
            sesion.add(d)
        except Exception("Error al guardar"):
            print("Repositorio de Dimension")
        return

    def recuperar(self, ov):
        try:
            sesion = self.contexto.sesion
            dimension_dto = sesion.query(ElementoDTO).filter_by(tipo_dimension=ov.tipo_dimension,\
                                                                valor_dimension=ov.valor_dimension)[0]
            dimension = self._mapeador.dto_a_entidad(dimension_dto)
        except Exception("Error al recuperar"):
            dimension = None
            print("Repositorio de Elemento")
        return dimension

    def eliminar(self, ov):
        pass

    def validar_existencia(self, ov):
        try:
            sesion = self.contexto.sesion
            dimension_dto = sesion.query(ElementoDTO).filter_by(tipo_dimension=ov.tipo_dimension,\
                                                                valor_dimension=ov.valor_dimension,\
                                                                id_elemento=ov.id_elemento)[0]
            if dimension_dto is  None:
                return False
            else:
                return True

        except Exception("Error al recuperar"):
            print("Repositorio de Dimension")
        return False

    def recuperar_por_tipo(self, tipo):
        pass

    def obtener_todo(self):
        pass
