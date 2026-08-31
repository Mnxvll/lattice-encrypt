import re
from Token import Token

class LatticeLexer:
    def __init__(self):
        # Diccionario de símbolos matemáticos y puntuación
        self.simbolos = {
            "+": "SUMA",
            "-": "RESTA",
            "=": "IGUAL",
            "*": "POR",
            "(": "IPAREN",
            ")": "DPAREN",
            "[": "ICORCH",
            "]": "DCORCH",
            "{": "ILLAVE",
            "}": "DLLAVE",
            ".": "PUNTO",
            ",": "COMA",
            ":": "DOSPUNTOS",
            ";": "PUNTILLO",
            "\"": "COMILLA",
            "'": "APOSTROFE",
            "!": "EXCLAMACION",
            "%": "PORCENTAJE",
            "/": "DIVISION",
        }

        # Diccionario de palabras reservadas
        self.palabras_reservadas = {
            "M": "MATRIZ",
            "MM": "MATRIZ_PRIVADA",
            "V": "VECTOR",
            "R": "RUIDO",
            "C": "CIFRADO",
            "def": "DEFINIR",
            "return": "RETORNAR",
            "for": "PARA",
            "in": "EN",
            "range": "RANGO",
            "len": "LONGITUD",
            "while": "MIENTRAS",
            "if": "SI",
            "else": "SINO",
            "append": "AGREGAR",
            "round": "REDONDEAR",
            "ord": "ORDINAL",
            "chr": "CARACTER",
            "int": "ENTERO",
            "random": "ALEATORIO",
            "randint": "ENTERO_ALEATORIO"
        }

    def tokenizar(self, texto):
        tokens = []
        i = 0
        n = len(texto)
        
        while i < n:
            char = texto[i]

            # Ignorar espacios en blanco
            if char.isspace():
                i += 1
                continue

            # Leer Letras (Palabras Reservadas o variables)
            if char.isalpha():
                inicio = i
                while i < n and texto[i].isalpha():
                    i += 1
                palabra = texto[inicio:i]
                
                if palabra in self.palabras_reservadas:
                    tokens.append(Token(self.palabras_reservadas[palabra], palabra))
                else:
                    tokens.append(Token("IDENTIFICADOR", palabra))
                continue
                
            # Leer números enteros y decimales    
            if char.isdigit():
                inicio = i 
                while i < n and (texto[i].isdigit() or texto[i] == "."):
                    i += 1
                numero = texto[inicio:i]
                tokens.append(Token("NUMERO", numero))
                continue

            # Leer Símbolos
            if char in self.simbolos:
                tokens.append(Token(self.simbolos[char], char))
                i += 1
                continue

            raise SyntaxError(f"Carácter inesperado: {char} en la posición {i}")    
            
        return tokens

if __name__ == "__main__":
    print(" Analizador Léxico Lattice ")
    lexer = LatticeLexer()
    
    while True:
        try:
            # Entrada por consola
            codigo_prueba = input(">> ")
            
            if codigo_prueba.strip().lower() == "salir":
                print("Saliendo del analizador...")
                break
            
            if not codigo_prueba.strip():
                continue
                
            # Tokenizar e imprimir
            mis_tokens = lexer.tokenizar(codigo_prueba)
            
            for t in mis_tokens:
                print(t)
                
        except SyntaxError as e:
            print(f"❌ {e}")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
