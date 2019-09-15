"""

"""
from analisis_proyectos.aplicacion.gestores.gestor_proyecto import *
from analisis_proyectos.infraestructura.persistencia.contexto.contexto_database_sqlite import *
from analisis_proyectos.infraestructura.persistencia.repositorios.DB_repositorio_proyecto import *
from analisis_proyectos.infraestructura.persistencia.mapeador.proyecto import *

# Crea el contexto para el repositorio de la entidades
mi_contexto = ContextoDBSQLite('sqlite:///proyectos.sqlite')

# Crea el gestor de la entidad
gestor = GestorProyecto()

mi_repositorio = DBRepositorioProyecto(mi_contexto, MapeadorDatosProyecto(mi_contexto))
gestor.asignar_repositorio(mi_repositorio)

#nombre_proyecto = NombreProyecto('Sistema de Gestión de Flota')
#gestor.crear_proyecto(nombre_proyecto, "DESARROLLO", "Sin Descripcion", "")
#gestor.guardar_proyecto()

otro_proyecto = gestor.recuperar_proyecto_por_nombre('Sistema de Gestión de Flota')
print(otro_proyecto)


