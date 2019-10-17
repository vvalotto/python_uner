from analisis_proyectos.dominio.analitico.muestra import *
from analisis_proyectos.dominio.analitico.analizador import *

if __name__ == "__main__":
    muestra = Muestra()

    repositorio = "C:/Users/vvalotto/PycharmProjects/python_uner/analisis_proyectos/presentacion/proyectos.sqlite"
    datos_origen = "SELECT * FROM mediciones_proyecto;"
    muestra.cargar_valores_de_muestra(repositorio, datos_origen)
    analizador = Analizador(muestra)

    esfuerzo_total = muestra.obtener_esfuerzo_total_proyecto("")
    print("Esfuerzo total del proyecto: %5.2f Horas o %5.2f PM" %(esfuerzo_total, (esfuerzo_total/152) ))

    esfuerzos = muestra.obtener_esfuerzo_por_actividad("")
    for actividad, esfuerzo in esfuerzos.items():
        print('Para ' + str(actividad)+ ": " + str(esfuerzo) + " horas")

    x = muestra.obtener_dimensiones_proyecto("")
    y = muestra.obtener_clases_CU("")

    print(x)
    print(y)

    print(analizador.productividad)

    distribucion = analizador.calcular_distribucion_esfuerzo()

    print(distribucion)
    analizador.clasificar_tamanio(x, y)
    print(analizador.predicir_tamanio(1, 1, 0)[0])