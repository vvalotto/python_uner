"""
--------------------------
Proyecto = ddd-evaluaciones
Modulo = prueba_arbol
Autor = admin
Fecha creación = 23/10/16
--------------------------
"""
from estructura_academica.dominio.general.estructura_geografica import *




if __name__ == '__main__':

    pais = Pais(Region("País", "Argentina"))
    print(pais)

    provincia = Provincia(Region("Provincia", "Entre Ríos"))
    print(provincia)
    pais.agregar_provincia(provincia)

    provincia = Provincia(Region("Provincia", "Santa Fe"))
    print(provincia)
    pais.agregar_provincia(provincia)

    for p in pais.provincias:
        print(p)


    print(pais.tiene_provincia("Cordoba"))