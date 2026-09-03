from LatticeLexico import Lexico
from LatticeSintactico import Sintactico

texto = "VECTOR(1,2) SUMA VECTOR(3,4)"

tokens = Lexico().tokenizar(texto) 

print(tokens)

analizadorSintactico = Sintactico(tokens)

resultado = analizadorSintactico.analisisSintactico()

print(resultado)

