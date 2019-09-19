
from analisis_proyectos.infraestructura.persistencia.contexto.contexto_database_sqlite import *
from analisis_proyectos.infraestructura.persistencia.mapeador.elemento import *
from analisis_proyectos.infraestructura.persistencia.repositorios.DB_repositorio_elemento import *

from analisis_proyectos.aplicacion.gestores.gestor_elemento import *

# Crea el contexto para el repositorio de la entidades
mi_contexto = ContextoDBSQLite('sqlite:///proyectos.sqlite')

repo_elemento = DBRepositorioElemento(mi_contexto, MapeadorDatosElemento(mi_contexto))
gestor_elemento = GestorElemento()
gestor_elemento.asignar_repositorio(repo_elemento)
CU = gestor_elemento.recuperar_elemento_por_nombre("CU100")
print(CU)

"""
gestor_elemento.dimensionar_elemento("PCU", 5)
gestor_elemento.dimensionar_elemento("Escenario", 3)
gestor_elemento.dimensionar_elemento("Entidades", 2)
gestor_elemento.dimensionar_elemento("Interfaces", 1)
gestor_elemento.dimensionar_elemento("PF", 6)

tipo_dim = TipoDimension("Interfaces")
dim = Dimension(tipo_dim, 4, CU.identificacion)

gestor_elemento.sacar_dimension(CU.lista_dimensiones[1][0])
gestor_elemento.cambiar_dimension(dim)

print(CU.lista_dimensiones)

for dim in CU.lista_dimensiones:
    print(dim[0], dim[1], dim[0].identificacion_elemento)

gestor_elemento.guardar_elemento()
"""
gestor_elemento.recuperar_dimensiones()
