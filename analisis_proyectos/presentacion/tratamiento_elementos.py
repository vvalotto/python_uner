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
modulo = gestor_componente.recuperar_componente_por_nombre("Entidades")
print(modulo)
print(modulo.identificacion)

#Crear gestor de elementos
repo_elemento = DBRepositorioElemento(mi_contexto, MapeadorDatosElemento(mi_contexto))
gestor_elemento = GestorElemento()
gestor_elemento.asignar_repositorio(repo_elemento)

cu = NombreElemento("Administrar Proveedor")
gestor_elemento.crear_elemento(cu, "Caso de Uso", "Sin Descripción", modulo.identificacion)
gestor_elemento.guardar_elemento()

cu = NombreElemento("Administrar Acreedor")
gestor_elemento.crear_elemento(cu, "Caso de Uso", "Sin Descripción", modulo.identificacion)
gestor_elemento.guardar_elemento()

cu = NombreElemento("Administrar Rol")
gestor_elemento.crear_elemento(cu, "Caso de Uso", "Sin Descripción", modulo.identificacion)
gestor_elemento.guardar_elemento()

cu = NombreElemento("Modificar Contraseña de Usuario")
gestor_elemento.crear_elemento(cu, "Caso de Uso", "Sin Descripción", modulo.identificacion)
gestor_elemento.guardar_elemento()

cu = NombreElemento("Administrar Usuario")
gestor_elemento.crear_elemento(cu, "Caso de Uso", "Sin Descripción", modulo.identificacion)
gestor_elemento.guardar_elemento()

cu = NombreElemento("Login")
gestor_elemento.crear_elemento(cu, "Caso de Uso", "Sin Descripción", modulo.identificacion)
gestor_elemento.guardar_elemento()

cu = NombreElemento("Administrar Estados")
gestor_elemento.crear_elemento(cu, "Caso de Uso", "Sin Descripción", modulo.identificacion)
gestor_elemento.guardar_elemento()

cu = NombreElemento("Administrar Maestro de Estados")
gestor_elemento.crear_elemento(cu, "Caso de Uso", "Sin Descripción", modulo.identificacion)
gestor_elemento.guardar_elemento()




