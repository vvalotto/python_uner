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
        self._muestra.obtener_tamanio_ucp("")
        return self._muestra.obtener_esfuerzos("") / self._muestra.obtener_tamanio_ucp("")

    def __init__(self, muestra):
        self._muestra = muestra
        return

    def calcular_densidad_de_defectos(self):
        return

    def calcular_distribucion_esfuerzo(self):
        esfuerzo_total = self._muestra.obtener_esfuerzos("")
        esfuerzos = self._muestra.esfuerzo_por_actividad("")
        distribucion = []
        return

    def clasificar_tamanio(self, X, Y):
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20)
        scaler = StandardScaler()
        scaler.fit(X_train)
        X_train = scaler.transform(X_train)
        X_test = scaler.transform(X_test)
        classifier = KNeighborsClassifier(n_neighbors=5)
        classifier.fit(X_train, y_train)

        return

    def predicir_tamanio(self):
        return

