from analisis_proyectos.dominio.entidades.elemento import *


nombre_elemento = NombreElemento('CU100')
elemento = Elemento(nombre_elemento, 'Caso de Uso', "Descripcion", "1")

tipo_dim = TipoDimension('PCU')
dimension = Dimension(tipo_dim, 5, elemento.identificacion)
elemento.agregar_dimension(dimension)
tipo_dim = TipoDimension('Escenarios')
dimension = Dimension(tipo_dim, 10, elemento.identificacion)
elemento.agregar_dimension(dimension)
tipo_dim = TipoDimension('Entidades')
dimension = Dimension(tipo_dim, 5, elemento.identificacion)
elemento.agregar_dimension(dimension)

print(elemento)
print(elemento.lista_dimensiones)

tipo_dim = TipoDimension("PCU")
dimension = Dimension(tipo_dim, 5, elemento.identificacion)
elemento.modificar_dimension(dimension)
print(elemento.lista_dimensiones)

elemento.eliminar_dimension(dimension)
print(elemento.lista_dimensiones)