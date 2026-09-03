"""Main entry point for testing the lexer and parser."""
from LatticeLexico import Lexico
from LatticeSintactico import Sintactico

print("=== Intérprete Lattice Encrypt ===")
print("Escribe un comando o 'salir' para terminar).")
print("Ejemplos:")
print("  VECTOR(1,2) SUMA VECTOR(3,4)")
print("  MATRIZ(2,0,0,2) POR VECTOR(3,4)")
print("  VECTOR(1,2) PUNTO VECTOR(3,4)")

while True:
    try:
        texto = input("\n>> ")
        if texto.strip().lower() == "salir":
            break
        if not texto.strip():
            continue

        analizadorLexico = Lexico()
        tokens = analizadorLexico.tokenizar(texto)
        
        analizadorSintactico = Sintactico(tokens)
        resultado = analizadorSintactico.analisisSintactico()

        print(f"\n[LÉXICO] Tokens generados: {tokens}\n")   

        print(f"Resultado: {resultado}")

    except Exception as e:
        print(f"Error: {e}")
