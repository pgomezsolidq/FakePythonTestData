# FakePythonData
PoC generating fake data with python for PowerBI

La idea es generar una estructura de entidades relacionadas en un (o varios) JSON que permitan crear una lógica pre-hoc para poder verla reflejada después en PowerBI.
La estrategia será basarnos en el módulo faker de python, que nos da opción de generar cosas como nombres, apellidos, nombres de compañías... para generar entidades con apariencia de reales.
Próximos pasos: separar las entidades y ampliar la lógica aplicada.

## Stage 1
La carpeta Stage 1 contiene el código tal y como queda despés del primer tutorial. Tras él, podemos generar archivos json que contienen un array de personas, y cada persona contiene un array de operaciones que hacen referencia a entidades tienda que no se materializan en el json. 

## Stage 2
Ampliamos las características del generador añadiendo algunas relaciones entre entidades, como por ejemplo, que las personas compren mayoritariamente en su ciudad (salvo que sean muy viajeros) y tamizamos las operaciones para los periodos de rebajas y vacaciones.
