"""
Clase que inicializa y arma las instancias necesarias iniciales de la aplicaccion:
Contextos de datos
Respositorios
Gestores
"""
from analisis_proyectos.infraestructura.persistencia.contexto.contexto_database_sqlite import *
from analisis_proyectos.infraestructura.persistencia.repositorios.DB_repositorio_proyecto import *
from analisis_proyectos.infraestructura.persistencia.mapeador.proyecto import *
from analisis_proyectos.aplicacion.gestores.gestor_proyecto import *
from analisis_proyectos.aplicacion.gestores.gestor_componente import *
from analisis_proyectos.aplicacion.gestores.gestor_elemento import *
from analisis_proyectos.dominio.analitico.muestra import *
from analisis_proyectos.dominio.analitico.analizador import *

import os
directorio_base = os.path.abspath(os.path.dirname(__file__))
URI_DATABASE = 'sqlite:///' + os.path.join(directorio_base, 'proyectos.sqlite')


class Configurador:

    contexto = ContextoDBSQLite(URI_DATABASE)
    repositorio_proyecto = DBRepositorioProyecto(contexto, MapeadorDatosProyecto(contexto))
    repositorio_componente = DBRepositorioComponente(contexto, MapeadorDatosComponente(contexto))
    repositorio_elemento = DBRepositorioElemento(contexto, MapeadorDatosElemento(contexto))
    gestor_proyecto = GestorProyecto()
    gestor_proyecto.asignar_repositorio(repositorio_proyecto)
    gestor_componente = GestorComponente()
    gestor_componente.asignar_repositorio(repositorio_componente)
    gestor_elemento = GestorElemento()
    gestor_elemento.asignar_repositorio(repositorio_elemento)

    muestra_proyectos=Muestra()
    analizador_proyecto = Analizador(muestra_proyectos)
    repositorio = "proyectos.sqlite"
    datos_origen = "SELECT * FROM mediciones_proyecto;"
    muestra_proyectos.cargar_valores_de_muestra(repositorio, datos_origen)


if __name__ == '__main__':
    print(Configurador.contexto.recurso)
    if Configurador.gestor_proyecto.existe_proyecto("Sistema de Gestión de Flota"):
        proyecto = Configurador.gestor_proyecto.recuperar_proyecto_por_nombre("Sistema de Gestión de Flota")
        print(proyecto)

