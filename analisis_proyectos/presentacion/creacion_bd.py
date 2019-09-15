#Crea el contexto con el motor sqlite y base de datos
from analisis_proyectos.infraestructura.persistencia.contexto.contexto_database_sqlite import *

DBEvaluacion = ContextoDBSQLite('sqlite:///proyectos.sqlite')

#Crea la tablas
DBEvaluacion.inicializar_tablas()

