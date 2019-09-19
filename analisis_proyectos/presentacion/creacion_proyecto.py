"""

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

# Crea el gestor de la entidad
gestor = GestorProyecto()

mi_repositorio = DBRepositorioProyecto(mi_contexto, MapeadorDatosProyecto(mi_contexto))
gestor.asignar_repositorio(mi_repositorio)

#nombre_proyecto = NombreProyecto('Sistema de Gestión de Flota')
#gestor.crear_proyecto(nombre_proyecto, "DESARROLLO", "Sin Descripcion", "")
#gestor.guardar_proyecto()

otro_proyecto = gestor.recuperar_proyecto_por_nombre('Sistema de Gestión de Flota')
print(otro_proyecto)
print(otro_proyecto.identificacion)

repo_componente = DBRepositorioComponente(mi_contexto, MapeadorDatosComponente(mi_contexto))
gestor_componente = GestorComponente()
gestor_componente.asignar_repositorio(repo_componente)
lista_componentes = gestor_componente.obtener_componentes_del_proyecto(otro_proyecto.identificacion)
print('Componentes ---->')
print(lista_componentes)

modulo_vehiculos = lista_componentes[1]

print(modulo_vehiculos)
nombre_elemento = NombreElemento("CU100")
mi_elemento = Elemento(nombre_elemento, "Caso de Uso", "Sin descricion", modulo_vehiculos.identificacion)
print(mi_elemento)
gestor_elemento = GestorElemento()
repo_elemento = DBRepositorioElemento(mi_contexto, MapeadorDatosElemento(mi_contexto))
gestor_elemento.asignar_repositorio(repo_elemento)
gestor_elemento.crear_elemento(nombre_elemento, "Caso de Uso", "Sin descricion", modulo_vehiculos.identificacion)
gestor_elemento.guardar_elemento()

