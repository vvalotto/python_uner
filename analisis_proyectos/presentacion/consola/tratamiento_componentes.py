"""
Altas de componentes
"""
from analisis_proyectos.aplicacion.gestores.gestor_proyecto import *
from analisis_proyectos.aplicacion.gestores.gestor_componente import *
from analisis_proyectos.aplicacion.gestores.gestor_elemento import *

from analisis_proyectos.infraestructura.persistencia.contexto.contexto_database_sqlite import *

from analisis_proyectos.infraestructura.persistencia.repositorios.DB_repositorio_proyecto import *
from analisis_proyectos.infraestructura.persistencia.repositorios.DB_repositorio_componente import *
from analisis_proyectos.infraestructura.persistencia.repositorios.DB_repositorio_elemento import *

from analisis_proyectos.infraestructura.persistencia.mapeador.proyecto import *
from analisis_proyectos.infraestructura.persistencia.mapeador.componente import *
from analisis_proyectos.infraestructura.persistencia.mapeador.elemento import  *

# Crea el contexto para el repositorio de la entidades
mi_contexto = ContextoDBSQLite('sqlite:///proyectos.sqlite')

# Crea el gestor de Proyecto
gestor = GestorProyecto()

mi_repositorio_proyecto = DBRepositorioProyecto(mi_contexto, MapeadorDatosProyecto(mi_contexto))
gestor.asignar_repositorio(mi_repositorio_proyecto)
proyecto = gestor.recuperar_proyecto_por_nombre('Sistema de Gestión de Flota')
print(proyecto)
print(proyecto.identificacion)

#Crea gestor de componente
repo_componente = DBRepositorioComponente(mi_contexto, MapeadorDatosComponente(mi_contexto))
gestor_componente = GestorComponente()
gestor_componente.asignar_repositorio(repo_componente)

# Creacion componente
nombre_modulo = NombreComponente("Gastos")
gestor_componente.crear_componente(nombre_modulo, "Módulo", proyecto.identificacion)
gestor_componente.guardar_componente()
