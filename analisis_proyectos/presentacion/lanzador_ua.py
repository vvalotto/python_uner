"""

"""
from estructura_academica.aplicacion.gestores.gestor_unidad_academica import *
from estructura_academica.infraestructura.persistencia.contexto.contexto_database import *
from estructura_academica.infraestructura.persistencia.repositorios.DB_repositorio_unidad_academica import *
from estructura_academica.infraestructura.persistencia.mapeador.unidad_academica import *

# Crea el contexto para el repositorio de la entidades
mi_contexto = ContextoDBMySQL('mysql+pymysql://pysea_admin:pysea@localhost:3306/pysea')

# Crea el gestor de la entidad
gestor = GestorUnidadAcademica()


mi_repositorio = DBRepositorioUnidadAcademica(mi_contexto, MapeadorDatosUnidadAcademica(mi_contexto))
gestor.asignar_repositorio(mi_repositorio)

"""
mi_ua = gestor.recuperar_unidad_academica_por_nombre('Facultad Regional Paraná')

print(mi_ua.nombre)
print(mi_ua.identificacion)
print(mi_ua.universidad)
print(mi_ua.domicilio)

cambia_nombre_ua = NombreUnidadAcademica('FRP')
cambia_universidad_ua = NombreUniversidad('UTN')

mi_ua.nombre = cambia_nombre_ua
mi_ua.universidad = cambia_universidad_ua

print(mi_ua)
# ------------------------------------


# Guarda la Unidad Academica

gestor.guardar_unidad_academica()

nombre = NombreUnidadAcademica('FCyT')
universidad = NombreUniversidad('UADER')
domicilio = Domicilio('Ruta 11', 'Km 10', ' ', ' ')

gestor.crear_unidad_academica(nombre, universidad, domicilio)
gestor.guardar_unidad_academica()
"""

print(gestor.recuperar_unidad_academica_por_nombre('Facultad Regional Paraná'))
print(gestor.recuperar_unidad_academica_por_nombre('Facultad Regional Paraná').identificacion)

print(gestor.existe_unidad_academica('FCYT'))

for unidad in gestor.obtener_todas_las_unidades_academicas():
    print(unidad)





