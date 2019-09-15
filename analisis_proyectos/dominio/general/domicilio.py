"""
--------------------------
Proyecto = ddd-evaluaciones
Modulo = domicilio
Autor = admin
Fecha creación = 16/10/16
--------------------------
"""
from estructura_academica.dominio.base.objeto_valor import *
from estructura_academica.dominio.base.texto_no_vacio import *

'''
Value Object: Direccion
'''


class Calle(TextoNoVacio):
    pass


class Numero(TextoNoVacio):

    def __init__(self, numero="Sin Numero"):
        super().__init__(numero)
        return


class Piso(TextoNoVacio):

    def __init__(self, piso="Sin Piso"):
        super().__init__(piso)
        return


class Departamento(TextoNoVacio):
    def __init__(self, departamento="Sin Departamento"):
        super().__init__(departamento)
        return


class Domicilio(ObjetoValor):

    @property
    def calle(self):
        return self._calle

    @property
    def numero(self):
        return self._numero

    @property
    def piso(self):
        return self._piso

    @property
    def departamento(self):
        return self._departamento

    def __init__(self, calle
                    , numero
                    , piso
                    , departamento):

        self._calle = calle
        self._numero = numero
        self._piso = piso
        self._departamento = departamento

        return

    def obtener_atributos_incluidos_en_chequeo_igualdad(self):
        return [self._calle, self._numero, self._departamento, self._piso]

    def __repr__(self):
        return \
            "Domicilio: " + "\n" + \
            "  " + str(self._numero) + "\n" + \
            "  " + str(self._calle) + "\n" + \
            "  " + str(self._departamento) + "\n" + \
            "  " + str(self._piso)

    def _validar_calle(self):
        pass

    def _validar_numero(self):
        pass

    def _validar_departamento(self):
        pass

    def _validar_piso(self):
        pass

