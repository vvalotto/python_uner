from estructura_academica.dominio.base.texto_no_vacio import *

texto = "a"
validacion = ValidadorTexto().validar(texto)
print(validacion.valido)
print(validacion.resultado)