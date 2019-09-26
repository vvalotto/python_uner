from analisis_proyectos.dominio.analitico.muestra import *

if __name__ == "__main__":
    muestra = Muestra()
    repositorio = "C:/Users/vvalotto/PycharmProjects/python_uner/analisis_proyectos/presentacion/proyectos.sqlite"
    datos_origen = "SELECT * FROM mediciones_proyecto;"
    muestra.cargar_valores_de_muestra(repositorio, datos_origen)

    print(muestra.obtener_esfuerzo_total_proyecto(""))

    esfuerzos = muestra.obtener_esfuerzo_por_actividad("")
    print(esfuerzos)

    print(muestra.obtener_dimensiones_proyecto(""))
    print(muestra.obtener_clases_CU(""))