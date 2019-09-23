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
modulo = gestor_componente.recuperar_componente_por_nombre("Ordenes")
print(modulo)
print(modulo.identificacion)

#Crear gestor de elementos
repo_elemento = DBRepositorioElemento(mi_contexto, MapeadorDatosElemento(mi_contexto))
gestor_elemento = GestorElemento()
gestor_elemento.asignar_repositorio(repo_elemento)


cu = gestor_elemento.recuperar_elemento_por_nombre("Dar de alta una Orden")
print(cu)
print(cu.identificacion)
print(cu.lista_dimensiones)
print(cu.lista_esfuerzos)
print(cu.lista_defectos)


#Agregar Dimensiones
gestor_elemento.dimensionar_elemento("Escenarios Definidos", 5)
gestor_elemento.dimensionar_elemento("Entidades Asociadas", 1)
gestor_elemento.dimensionar_elemento("Interfaces", 0)
gestor_elemento.dimensionar_elemento("Elementos", 8)
gestor_elemento.dimensionar_elemento("PF", 20)
gestor_elemento.dimensionar_elemento("UCP", 5)
print(cu.lista_dimensiones)

#Agregar Esfuezos

gestor_elemento.registrar_esfuerzo("Análisis", 6.75)
gestor_elemento.registrar_esfuerzo("Diseño", 7.25)
gestor_elemento.registrar_esfuerzo("Programación",23.25)
gestor_elemento.registrar_esfuerzo("Retrabajo", 0)
gestor_elemento.registrar_esfuerzo("Revisión", 0.5)
gestor_elemento.registrar_esfuerzo("Testing", 1.33)
print(cu.lista_esfuerzos)


#Agregar defectos
gestor_elemento.registrar_defecto("CASOS_DE_PRUEBA", 9)
gestor_elemento.registrar_defecto("TEST_FUNCIONAL",5)
gestor_elemento.registrar_defecto("TEST_USUARIO", 5)
print(cu.lista_defectos)

print(cu.lista_dimensiones)
print(cu.lista_esfuerzos)
print(cu.lista_defectos)

gestor_elemento.guardar_elemento()