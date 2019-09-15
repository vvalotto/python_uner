"""
--------------------------
Proyecto = ddd-evaluaciones
Modulo = ubicacion
Autor = admin
Fecha creación = 29/10/16
--------------------------
"""

from estructura_academica.dominio.general.domicilio import *
from .objeto_valor import *


class Ubicacion(ObjetoValor):

    @property
    def domicilio(self):
        return self._domicilio

    @property
    def pais(self):
        return self._pais

    @property
    def provincia(self):
        return self._provincia

    @property
    def ciudad(self):
        return self._ciudad

    @property()
    def codigo_postal(self):
        return self._codigo_postal

    def __init__(self, domicilio,
                       pais,
                       provincia,
                       ciudad,
                       codigo_postal):

        try:
            self._validar_domicilio(domicilio)
            self._validar_pais(pais)
            self._validar_provincia(provincia)
            self._validar_ciudad(ciudad)
            self._validar_codigo_postal(codigo_postal)
        except:
            raise

        self._domicilio = domicilio
        self._pais = pais
        self._provincia = provincia
        self._ciudad = ciudad
        self._codigo_postal = codigo_postal

        return

    def _validar_domicilio(self, domicilio):
        return True

    def _validar_pais(self, pais):
        return True

    def _validar_provincia(self, provincia):
        return True

    def _validar_ciudad(self, ciudad):
        return True

    def _validar_codigo_postal(self, codigo_postal):
        return True







