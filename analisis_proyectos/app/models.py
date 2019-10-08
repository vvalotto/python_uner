from ..aplicacion.gestores.gestor_proyecto import *
from ..aplicacion.gestores.gestor_componente import *

from .configurador import *

class ProyectoVM:

    @property
    def nombre(self):
        return self._nombre

    @property
    def descripciom(self):
        return self._descripcion

    @property
    def lista(self):
        return self._modulos

    def __init__(self, gestor):
        self._gestor = gestor
        self._id = None
        self._nombre = None
        self._descripcion = None
        self._tipo = None
        self._modulos = []
        return

    def existe_proyecto(self, nombre):
       if self._gestor.existe_proyecto(nombre):
           return True
       else:
           return False

    def obtener_proyecto(self, nombre):
        proyecto = self._gestor.recuperar_proyecto_por_nombre(nombre)
        self._id = proyecto.identificacion
        self._nombre = nombre
        self._descripcion = proyecto.descripcion
        self._tipo = proyecto.tipo_proyecto
        return

    def listar_modulos(self):
        repo_componente = DBRepositorioComponente(Configurador.contexto, MapeadorDatosComponente(Configurador.contexto))
        gestor_componente = GestorComponente()
        gestor_componente.asignar_repositorio(repo_componente)
        lista_componentes = gestor_componente.obtener_componentes_del_proyecto(self._id)
        for componente in lista_componentes:
            self._modulos.append(componente)
        return

class ComponenteVM:

    def __init__(self):
        return


class ElementoVM:

    def __init__(self):
        return


