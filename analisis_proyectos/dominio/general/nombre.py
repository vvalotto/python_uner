"""
--------------------------
Proyecto = ddd-evaluaciones
Modulo = nombre
Autor = admin
Fecha creación = 22/10/16
--------------------------
"""

from estructura_academica.dominio.base.objeto_valor import *


class Nombre(ObjetoValor):

    """
    Propiedades accedidas
    """
    @property
    def nombres(self):
        return self._nombres

    @property
    def apellido(self):
        return self._apellido

    def __init__(self, nombres='Sin Nombre', apellido ='Sin Apellido'):
        """
        Creación del objeto valor nombre
        :param nombres:
        :param apellido:
        """
        if nombres is None:
            raise Exception("No hay Mombre")
        if apellido is None:
            raise Exception("no hay apellido")

        self._nombres = nombres
        self._apellido = apellido
        return

    def apellido_y_nombres(self):
        """
        Se devuelve de la manera apellido y nombre
        :return:
        """
        return self._apellido + ', ' + self._nombres

    def __repr__(self):
        return  self.nombre + ' ' + self.apellido
