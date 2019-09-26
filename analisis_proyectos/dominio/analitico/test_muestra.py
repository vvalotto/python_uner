from unittest import TestCase
from .muestra import *

class TestMuestra(TestCase):

    def setUp(self) -> None:
        self._muestra = Muestra()
        return

    def test_cargar_valores_de_muestra(self):
        repositorio = "C:/Users/vvalotto/PycharmProjects/python_uner/analisis_proyectos/presentacion/proyectos.sqlite"
        datos_origen = "SELECT * FROM mediciones_proyecto;"
        self._muestra.cargar_valores_de_muestra(repositorio, datos_origen)
        

    def test_obtener_matriz_valores(self):
        self.fail()

    def test_obtener_tamanio_en_ucp(self):
        self.fail()

    def test_obtener_esfuerzo_total_proyecto(self):
        self.fail()

    def test_obetner_esfuerzo_por_actividad(self):
        self.fail()

    def test_obtener_dimensiones_proyecto(self):
        self.fail()
