"""

"""

import unittest2
from estructura_academica.dominio.base.texto_no_vacio import *


class TestTextoNoVacio(unittest2.TestCase):

    def test_texto_no_vacio(self):
        mi_texto = TextoNoVacio("Hola")
        self.assertEqual(mi_texto.texto, "Hola")
        return

    def test_texto_vacio(self):
        self.assertRaises(Exception, TextoNoVacio, "")
        return

    def test_texto_null(self):
        txt = None
        self.assertRaises(Exception, TextoNoVacio, txt)
        return
