# Interprete Lattice Encrypt

Interprete diseñado para ejecutar operaciones matematicas orientadas a la criptografia basada en reticulos (Lattice Cryptography), especificamente el algoritmo LWE (Learning With Errors). El lenguaje permite realizar operaciones sobre matrices y vectores, inyeccion de ruido, redondeo, y cifrado/descifrado de informacion.

## Estructura del Proyecto

El proyecto se divide en los siguientes modulos principales:

*   **LatticeLexico.py**: Contiene el Analizador Lexico (`Lexico`). Se encarga de leer el texto de entrada caracter por caracter y agruparlos en Tokens validos (palabras reservadas, numeros y simbolos).
*   **LatticeSintactico.py**: Contiene el Analizador Sintactico (`Sintactico`). Recibe la lista de tokens del analizador lexico y comprueba que cumplan las reglas gramaticales del lenguaje. Adicionalmente, incluye metodos para ejecutar las operaciones matematicas correspondientes.
*   **Token.py**: Define la estructura de datos `Token` utilizada para transportar informacion entre el analizador lexico y el sintactico. Almacena el tipo de token y su valor literal.
*   **Runner.py**: Punto de entrada del programa. Permite definir instrucciones en texto, pasarlas por el proceso lexico, luego por el sintactico y mostrar el resultado por consola.
*   **reglas.json**: Archivo de configuracion del despachador dinamico. Define los grupos de operaciones permitidas y que funcion especifica del analizador sintactico debe llamarse para validar cada grupo.
*   **docs/**: Directorio que incluye documentacion teorica, incluyendo diagramas de los automatas en formato Markdown/Mermaid (lexico para simbolos, palabras y un ejemplo sintactico de suma de vectores).

## Metodologia de Trabajo en Equipo

El proyecto utiliza un patron de despacho dinamico a traves de `reglas.json` para facilitar la extension del lenguaje. El flujo de trabajo consiste en:
1. Crear una nueva rama para implementar una categoria de operaciones.
2. Definir la regla en `reglas.json` asignando un metodo de ejecucion.
3. Desarrollar el metodo correspondiente en `LatticeSintactico.py`.
4. Realizar un Pull Request hacia la rama principal (main).
