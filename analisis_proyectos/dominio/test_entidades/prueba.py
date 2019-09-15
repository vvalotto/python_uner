"""
--------------------------
Proyecto = ddd-evaluaciones
Modulo = prueba
Autor = admin
Fecha creación = 16/10/16
--------------------------
"""

from analisis_proyectos.dominio.entidades.componente import *
from analisis_proyectos.dominio.entidades.proyecto import *
from analisis_proyectos.dominio.entidades.elemento import *

#Prueba entidad proyecto

nombre_proyecto = NombreProyecto("Sistema de Gestión de Flota")
desc_proyecto = DescripcionProyecto("Sin Descripcion")
mi_proyecto = Proyecto(nombre_proyecto, "DESARROLLO",desc_proyecto, None)
print(mi_proyecto)
print(mi_proyecto.fecha_fin)
print(mi_proyecto.identificacion)

#Prueba Entidad componente

nombre = NombreComponente("sgf")
mi_componente = Componente(nombre, "Aplicación", mi_proyecto.identificacion)

print(mi_componente)
print(mi_componente.identificacion)
print(mi_componente.identificacion_proyecto)

nombre = NombreComponente("Entidades")
mi_componente = Componente(nombre, "Módulo", mi_proyecto.identificacion)

print(mi_componente)
print(mi_componente.identificacion)
print(mi_componente.identificacion_proyecto)

nombre = NombreComponente("Controles")
mi_componente = Componente(nombre, "Módulo", mi_proyecto.identificacion)

print(mi_componente)
print(mi_componente.identificacion)
print(mi_componente.identificacion_proyecto)

nombre = NombreComponente("Vehículos")
mi_componente = Componente(nombre, "Módulo", mi_proyecto.identificacion)

print(mi_componente)
print(mi_componente.identificacion)
print(mi_componente.identificacion_proyecto)