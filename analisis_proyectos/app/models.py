from ..aplicacion.gestores.gestor_proyecto import *
from ..aplicacion.gestores.gestor_componente import *
from ..aplicacion.gestores.gestor_elemento import *

from .configurador import *

class ListaProyectoVM:

    def __init__(self, gestor):
        self._gestor = gestor
        self._proyectos = []
        return

    def obtener_proyectos(self):
        return self._gestor.obtener_todos_los_proyectos()


class ProyectoVM:

    @property
    def identificador(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @property
    def descripcion(self):
        return self._descripcion

    @property
    def tipo(self):
        return self._tipo

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
        self._modulos = []
        repo_componente = DBRepositorioComponente(Configurador.contexto, MapeadorDatosComponente(Configurador.contexto))
        gestor_componente = GestorComponente()
        gestor_componente.asignar_repositorio(repo_componente)
        lista_componentes = gestor_componente.obtener_componentes_del_proyecto(self._id)
        for componente in lista_componentes:
            self._modulos.append(componente)
        return

class ComponenteVM:

    @property
    def nombre(self):
        return self._nombre

    @property
    def tipo(self):
        return self._tipo_componente

    @property
    def lista_elementos(self):
        return self._elementos

    def __init__(self, gestor):
        self._gestor = gestor
        self._nombre = None
        self._tipo_componente = None
        self._id = None
        self._elementos = []
        return

    def existe_componente(self, nombre):
        if self._gestor.existe_componente(nombre):
            return True
        else:
            return False

    def obtener_componente(self, nombre):
        componente = self._gestor.recuperar_componente_por_nombre(nombre)
        self._id = componente.identificacion
        self._nombre = nombre
        self._tipo = componente.tipo_componente
        return

    def  listar_elementos(self):
        self._elementos = []
        repo_elemento = DBRepositorioElemento(Configurador.contexto, MapeadorDatosElemento(Configurador.contexto))
        gestor_elemento= GestorElemento()
        gestor_elemento.asignar_repositorio(repo_elemento)
        lista_componentes = gestor_elemento.obtener_elementos_del_componente(self._id)
        for componente in lista_componentes:
            self._elementos.append(componente)
        return

class ElementoVM:

    def __init__(self):
        pass



