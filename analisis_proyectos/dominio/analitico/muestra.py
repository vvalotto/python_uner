"""
Muestra para hacer análisis de datos de proyectos
"""
import sqlite3
import pandas as pd

class Muestra:

    def __init__(self):
        self._dataframe__muestra = None
        return

    def cargar_valores_de_muestra(self, repositorio, datos_origen):
        """
        accede al respositorio de datos y recupera la matriz de valores a tratar
        se lo asigna a un frame de pandas y lo compone dentro de la clase
        :param repositorio:
        :return:
        """
        con = sqlite3.connect(repositorio)
        cur = con.cursor()
        res = cur.execute(datos_origen)
        self._dataframe__muestra = pd.read_sql_query(datos_origen, con)
        cur.close()
        return

    def obtener_matriz_valores(self):
        """
        Retorno al frame de panda con los datos extriados
        :return:
        """
        return self._dataframe__muestra

    def obtener_tamanio_en_ucp(self, proyecto):
        return self._dataframe__muestra["Puntos_de_Casos_de_Uso"].sum()

    def obtener_esfuerzo_total_proyecto(self, proyecto):
        esfuerzo_total = self._dataframe__muestra["Esfuerzo_Analisis"].sum()
        esfuerzo_total = self._dataframe__muestra["Esfuerzo_Disenio"].sum() + esfuerzo_total
        esfuerzo_total = self._dataframe__muestra["Esfuerzo_Programacion"].sum() + esfuerzo_total
        esfuerzo_total = self._dataframe__muestra["Esfuerzo_Retrabajo"].sum() + esfuerzo_total
        esfuerzo_total = self._dataframe__muestra["Esfuerzo_Revision"].sum() + esfuerzo_total
        esfuerzo_total = self._dataframe__muestra["Esfuerzo_Testing"].sum() + esfuerzo_total
        return esfuerzo_total

    def obtener_esfuerzo_por_actividad(self, proyecto):
        esfuerzos = {"Analisis": self._dataframe__muestra["Esfuerzo_Analisis"].sum(),
                     "Disenio": self._dataframe__muestra["Esfuerzo_Disenio"].sum(),
                     "Programacion": self._dataframe__muestra["Esfuerzo_Programacion"].sum(),
                     "Retrabajo": self._dataframe__muestra["Esfuerzo_Retrabajo"].sum(),
                     "Revision": self._dataframe__muestra["Esfuerzo_Revision"].sum(),
                     "Testing": self._dataframe__muestra["Esfuerzo_Testing"].sum()}
        return esfuerzos

    def obtener_dimensiones_proyecto(self, proyecto):
        res = self._dataframe__muestra[['Escenarios','Entidades','Interfaces']].values
        return res

    def obtener_clases_CU(self, proyecto):
        res = self._dataframe__muestra['Puntos_de_Casos_de_Uso'].values
        return res

