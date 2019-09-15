"""
--------------------------
Proyecto = ddd-evaluaciones
Modulo = prueba_objeto_valor
Autor = admin
Fecha creación = 22/10/16
--------------------------
"""

from analisis_proyectos.dominio.base.objeto_valor import *

from analisis_proyectos.dominio.general.estructura_geografica import *


class Nombre(ObjetoValor):

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    def __init__(self, nombre='Sin Nombre', apellido ='Sin Apellido'):
        if nombre is None:
            raise ("no hay nombre")
        if apellido is None:
            raise ("no hay apellido")

        self._nombre = nombre
        self._apellido = apellido
        return

    def __str__(self):
        return  self.nombre + ' ' + self.apellido


if __name__ == '__main__':

    mi_pais = Pais('Argentina', None)
    mi_provincia = Provincia('Entre Ríos', mi_pais)
    otro_provincia = Provincia('Santa Fe', mi_pais)
    print(mi_pais)
    for provincia in mi_pais.regiones_hijas:
        print(provincia)
    print(mi_provincia)
    print(mi_pais.validar_si_contiene_region(mi_provincia))
    print(mi_pais.validar_si_contiene_region(otro_provincia))
    print(mi_pais.validar_si_contiene_region_por_nombre('Cordoba'))

