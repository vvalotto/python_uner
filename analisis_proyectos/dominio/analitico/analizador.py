"""
Generador de resultados del análisis
"""

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

class Analizador:

    @property
    def productividad(self):
        return self._muestra.obtener_esfuerzo_total_proyecto("") / self._muestra.obtener_tamanio_en_ucp("")

    def __init__(self, muestra):
        self._muestra = muestra
        self._clasificador = None
        return

    def calcular_densidad_de_defectos(self):
        return

    def calcular_esfuerzo_real(self):
        return self._muestra.obtener_esfuerzo_total_proyecto("")

    def calcular_tamanio_real(self):
        return self._muestra.obtener_tamanio_en_ucp("")

    def calcular_distribucion_esfuerzo(self):
        esfuerzo_total = self._muestra.obtener_esfuerzo_total_proyecto("")
        esfuerzos = self._muestra.obtener_esfuerzo_por_actividad("")
        distribucion = {}
        for key in esfuerzos.keys():
            distribucion[key] = (esfuerzos[key] / esfuerzo_total) * 100
        return distribucion

    def clasificar_tamanio(self, X, Y):
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20)
        scaler = StandardScaler()
        scaler.fit(X_train)
        X_train = scaler.transform(X_train)
        X_test = scaler.transform(X_test)
        self._clasificador = KNeighborsClassifier(n_neighbors=5)
        self._clasificador.fit(X_train, y_train)

        return

    def predicir_tamanio(self, escenarios, entidades, interfaces):
        return self._clasificador.predict([[escenarios, entidades, interfaces]])

