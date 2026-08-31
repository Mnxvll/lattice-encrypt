import random

class LatticeCipher:
    def __init__(self):
        # 1. PREPARACIÓN: Matriz Pública (Clave)
        # En la realidad esto es una matriz gigante y de números grandes.
        # Aquí usamos una matriz 4x4 de ejemplo.
        self.matriz_publica = [
            [2, 5, 1, 3],
            [1, 2, 4, 1],
            [3, 1, 1, 5],
            [4, 3, 2, 2]
        ]
        
        # La Clave Privada es la matriz inversa exacta de la Matriz Pública
        self.clave_privada = [
            [-0.1707317, -0.1463414, -0.0243902,  0.3902439],
            [ 0.2439024, -0.0195121, -0.1365853, -0.0146341],
            [-0.0975609,  0.2878048,  0.0146341, -0.0341463],
            [ 0.0731707,  0.0341463,  0.2390243, -0.2243902]
        ]

    def _letras_a_numeros(self, bloque_texto):
        """Convierte cada letra de un bloque de texto a su valor numérico (ASCII)"""
        return [ord(letra) for letra in bloque_texto]

    def _multiplicar_y_sumar(self, vector, matriz, ruido):
        """Simula la operación matemática principal de Lattice para cifrar"""
        resultado = [] 
        for col in range(len(matriz[0])):
            suma = 0
            for fila in range(len(vector)):
                suma += vector[fila] * matriz[fila][col]
            suma += ruido[col]
            resultado.append(suma)
        return resultado

    def _multiplicar_vector_matriz_decimal(self, vector, matriz):
        """Función inversa para descifrar usando la Clave Privada"""
        resultado = []
        for col in range(len(matriz[0])):
            suma = 0
            for fila in range(len(vector)):
                suma += vector[fila] * matriz[fila][col]
            # El redondeo elimina el "ruido"
            resultado.append(round(suma))
        return resultado

    def cifrar(self, texto):
        # Rellenamos el texto con espacios si no es múltiplo de 4
        while len(texto) % 4 != 0:
            texto += " "

        tokens_cifrados = []
        
        # Recorremos el texto en bloques de 4
        for i in range(0, len(texto), 4):
            bloque = texto[i : i+4]
            vector_mensaje = self._letras_a_numeros(bloque)
            
            # Generar Ruido
            ruido = [random.randint(-2, 2) for _ in range(4)]
            
            # Operación Lattice
            resultado_cifrado = self._multiplicar_y_sumar(vector_mensaje, self.matriz_publica, ruido)
            
            tokens_cifrados.append({
                "tipo": "BLOQUE_CIFRADO_LATTICE",
                "texto_original": bloque,
                "vector_cifrado": resultado_cifrado
            })
            
        return tokens_cifrados

    def descifrar(self, tokens_cifrados):
        mensaje_recuperado = ""
        
        for token in tokens_cifrados:
            vector = token["vector_cifrado"]
            vector_original = self._multiplicar_vector_matriz_decimal(vector, self.clave_privada)
            
            for num in vector_original:
                mensaje_recuperado += chr(int(num))
                
        return mensaje_recuperado


# 
# EJECUCIÓN PRINCIPAL DEL SCRIPT
# 

if __name__ == "__main__":
    cipher = LatticeCipher()
    
    mensaje = "LATAM UPTC"
    print(f"Mensaje original: '{mensaje}'\n")
    
    resultado = cipher.cifrar(mensaje)
    
    print("--- Tokens generados por Cifrado Lattice ---")
    for token in resultado:
        print(f"Bloque: '{token['texto_original']}' -> Cifrado: {token['vector_cifrado']}")

    print("\n--- Proceso de Descifrado ---")
    texto_final = cipher.descifrar(resultado)
    print(f"Mensaje recuperado: '{texto_final}'")
