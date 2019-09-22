
from analisis_proyectos.infraestructura.persistencia.contexto.contexto_database_sqlite import *
from analisis_proyectos.infraestructura.persistencia.mapeador.elemento import *
from analisis_proyectos.infraestructura.persistencia.repositorios.DB_repositorio_elemento import *

from analisis_proyectos.aplicacion.gestores.gestor_elemento import *

# Crea el contexto para el repositorio de la entidades
mi_contexto = ContextoDBSQLite('sqlite:///proyectos.sqlite')

repo_elemento = DBRepositorioElemento(mi_contexto, MapeadorDatosElemento(mi_contexto))
gestor_elemento = GestorElemento()
gestor_elemento.asignar_repositorio(repo_elemento)
