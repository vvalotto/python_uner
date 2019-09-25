import numpy as np
import pandas as pd
import sqlite3
import sklearn

vista = "SELECT * FROM mediciones_proyecto;"

con = sqlite3.connect("C:/Users/vvalotto/PycharmProjects/python_uner/analisis_proyectos/presentacion/proyectos.sqlite")
cur = con.cursor()
res = cur.execute(vista)

for fila in cur.fetchall():
    print(fila[2])

df = pd.read_sql_query(vista, con)
cur.close()

tamaño_total = df["Puntos_de_Casos_de_Uso"].sum()
esfuerzo_total = df["Esfuerzo_Analisis"].sum()
print(esfuerzo_total)
esfuerzo_total = df["Esfuerzo_Disenio"].sum() + esfuerzo_total
print(esfuerzo_total)
esfuerzo_total = df["Esfuerzo_Programacion"].sum() + esfuerzo_total
print(esfuerzo_total)
esfuerzo_total = df["Esfuerzo_Retrabajo"].sum() + esfuerzo_total
print(esfuerzo_total)
esfuerzo_total = df["Esfuerzo_Revision"].sum() + esfuerzo_total
print(esfuerzo_total)
esfuerzo_total = df["Esfuerzo_Testing"].sum() + esfuerzo_total
print(esfuerzo_total)

defectos_totales = df["Defectos_Test_Funcional"].sum()
defectos_totales = df["Defectos_Test_Usuarios"].sum() + defectos_totales

print(tamaño_total)
LOE = esfuerzo_total / tamaño_total

DENSIDAD_DE_DEFECTOS = defectos_totales / tamaño_total

print("LOE: %2.2f" % LOE)
print("DENSIDAD DE DEFECTOS: %2.2f" % DENSIDAD_DE_DEFECTOS)

X = df.iloc[:,4:7].values
print(X)

Y = df.iloc[:,3].values
print(Y)


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

print(classifier.predict([[0,0,0]]))