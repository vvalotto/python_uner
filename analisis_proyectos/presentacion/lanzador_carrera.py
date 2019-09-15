"""

"""
from estructura_academica.aplicacion.gestores.gestor_unidad_academica import *
from estructura_academica.aplicacion.gestores.gestor_carrera import *
from estructura_academica.infraestructura.persistencia.contexto.contexto_database import *
from estructura_academica.infraestructura.persistencia.repositorios.DB_repositorio_carrera import *
from estructura_academica.infraestructura.persistencia.repositorios.DB_repositorio_unidad_academica import *
from estructura_academica.infraestructura.persistencia.mapeador.carrera import *
from estructura_academica.infraestructura.persistencia.mapeador.unidad_academica import *

# Crea el contexto para el repositorio de la entidades
mi_contexto = ContextoDBMySQL('mysql+pymysql://pysea_admin:pysea@localhost:3306/pysea')

mi_gestor_unidad_academica = GestorUnidadAcademica()
mi_gestor_unidad_academica.asignar_repositorio(DBRepositorioUnidadAcademica
                                               (mi_contexto, MapeadorDatosUnidadAcademica(mi_contexto)))
mi_ua = mi_gestor_unidad_academica.recuperar_unidad_academica_por_nombre('Facultad de Ingeniería')

print(mi_ua)

# Crea el gestor de la entidad
mi_gestor_carrera = GestorCarrera()

mi_repositorio = DBRepositorioCarrera(mi_contexto, MapeadorDatosCarrera(mi_contexto))
mi_gestor_carrera.asignar_repositorio(mi_repositorio)

nombre = NombreCarrera('Licenciatura en Bioinformática')
codigo = CodigoCarrera('ING01')
unidad_academica = IdUnidadAcademica(mi_ua.identificacion)

print(mi_gestor_carrera.crear_carrera(nombre, codigo, unidad_academica))

# mi_gestor_carrera.guardar_carrera()

print(mi_gestor_carrera.recuperar_carrera_por_nombre('Licenciatura en Bioinformática'))

# for carrera in list(mi_gestor_carrera.obtener_todas_las_carreras_por_ua(mi_ua.identificacion)):
#    print(carrera)


