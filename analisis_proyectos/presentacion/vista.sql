SELECT DISTINCT
                nombre_componente,
                nombre_elemento,
                PF.valor_dimension AS Puntos_de_Funcion,
                UCP.valor_dimension AS Puntos_de_Casos_de_Uso,
                ESCENARIOS.valor_dimension AS Escenarios,
                ENTIDADES.valor_dimension AS Entidades,
                INTERFACES.valor_dimension AS Interfaces,
                ELEMENTOS.valor_dimension AS Elmentos,

                ESFUERZO_ANALISIS.esfuerzo_actividad AS Esfuerzo_Analisis,
                ESFUERZO_DISENIO.esfuerzo_actividad AS Esfuerzo_Disenio,
                ESFUERZO_PROGRAMACION.esfuerzo_actividad AS Esfuerzo_Programacion,
                ESFUERZO_RETRABAJO.esfuerzo_actividad AS Esfuerzo_Retrabajo,
                ESFUERZO_REVISION.esfuerzo_actividad AS Esfuerzo_Revision,
                ESFUERZO_TESTING.esfuerzo_actividad AS Esfuerzo_Testing,

                CASOS_DE_PRUEBA.cantidad_defecto AS Casos_de_Prueba,
                TEST_FUNCIONAL.cantidad_defecto AS Defectos_Test_Funcional,
                TEST_USUARIO.cantidad_defecto AS Defectos_Test_Usuarios

FROM td_elemento, td_componente,

(SELECT valor_dimension, id_elemento
FROM td_dimension_elemento
WHERE tipo_dimension = "PF") PF,
(SELECT valor_dimension, id_elemento
FROM td_dimension_elemento
WHERE tipo_dimension = "UCP") UCP,
(SELECT valor_dimension, id_elemento
FROM td_dimension_elemento
WHERE tipo_dimension = "Escenarios Definidos") ESCENARIOS,
(SELECT valor_dimension, id_elemento
FROM td_dimension_elemento
WHERE tipo_dimension = "Entidades Asociadas") ENTIDADES,
(SELECT valor_dimension, id_elemento
FROM td_dimension_elemento
WHERE tipo_dimension = "Interfaces") INTERFACES,
(SELECT valor_dimension, id_elemento
FROM td_dimension_elemento
WHERE tipo_dimension = "Elementos") ELEMENTOS,

(SELECT esfuerzo_actividad, id_elemento
FROM td_esfuerzo_elemento
WHERE tipo_actividad = "Análisis") ESFUERZO_ANALISIS,
(SELECT esfuerzo_actividad, id_elemento
FROM td_esfuerzo_elemento
WHERE tipo_actividad = "Diseño") ESFUERZO_DISENIO,
(SELECT esfuerzo_actividad, id_elemento
FROM td_esfuerzo_elemento
WHERE tipo_actividad = "Programación") ESFUERZO_PROGRAMACION,
(SELECT esfuerzo_actividad, id_elemento
FROM td_esfuerzo_elemento
WHERE tipo_actividad = "Retrabajo") ESFUERZO_RETRABAJO,
(SELECT esfuerzo_actividad, id_elemento
FROM td_esfuerzo_elemento
WHERE tipo_actividad = "Revisión") ESFUERZO_REVISION,
(SELECT esfuerzo_actividad, id_elemento
FROM td_esfuerzo_elemento
WHERE tipo_actividad = "Testing") ESFUERZO_TESTING,

(SELECT cantidad_defecto, id_elemento
FROM td_defecto_elemento
WHERE fase_defecto = "CASOS_DE_PRUEBA") CASOS_DE_PRUEBA,
(SELECT cantidad_defecto, id_elemento
FROM td_defecto_elemento
WHERE fase_defecto = "TEST_FUNCIONAL") TEST_FUNCIONAL,
(SELECT cantidad_defecto, id_elemento
FROM td_defecto_elemento
WHERE fase_defecto = "TEST_USUARIO") TEST_USUARIO



WHERE td_elemento.id = PF.id_elemento AND
      td_elemento.id = UCP.id_elemento AND
      td_elemento.id = ESCENARIOS.id_elemento AND
      td_elemento.id = ENTIDADES.id_elemento AND
      td_elemento.id = INTERFACES.id_elemento AND
      td_elemento.id = ELEMENTOS.id_elemento AND

      td_elemento.id = ESFUERZO_ANALISIS.id_elemento AND
      td_elemento.id = ESFUERZO_DISENIO.id_elemento AND
      td_elemento.id = ESFUERZO_PROGRAMACION.id_elemento AND
      td_elemento.id = ESFUERZO_RETRABAJO.id_elemento AND
      td_elemento.id = ESFUERZO_REVISION.id_elemento AND
      td_elemento.id = ESFUERZO_TESTING.id_elemento AND

      td_elemento.id = CASOS_DE_PRUEBA.id_elemento AND
      td_elemento.id = TEST_FUNCIONAL.id_elemento AND
      td_elemento.id = TEST_USUARIO.id_elemento AND

      td_elemento.id_componente = td_componente.id