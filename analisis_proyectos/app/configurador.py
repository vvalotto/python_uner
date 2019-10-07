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
import os
directorio_base = os.path.abspath(os.path.dirname(__file__))
URI_DATABASE = 'sqlite:///' + os.path.join(directorio_base, 'proyectos.sqlite')

class Configurador:

    contexto = ContextoDBSQLite(URI_DATABASE)
    repositorio_proyecto = DBRepositorioProyecto(contexto, MapeadorDatosProyecto(contexto))
    gestor_proyecto = GestorProyecto()
    gestor_proyecto.asignar_repositorio(repositorio_proyecto)



if __name__ == '__main__':
    print(Configurador.contexto.recurso)
    if Configurador.gestor_proyecto.existe_proyecto("Sistema de Gestión de Flota"):
        proyecto = Configurador.gestor_proyecto.recuperar_proyecto_por_nombre("Sistema de Gestión de Flota")
        print(proyecto)

