
class Sintactico:

    # Constructor      
    def __init__(self, tokens):
       self.tokens = tokens
       self.pos = 0


    # Metodo que retorna el token actual    
    def actual(self):
       if self.pos < len(self.tokens): # Si la posicion es menor a la longitud de los tokens
             return self.tokens[self.pos] # 
       return None


    # Metodo que consume el token actual si es del tipo esperado 
    def consumir(self, tipo):
        token = self.actual()        


        if token is None:   
            raise SyntaxError("No hay token")


        if token.tipo != tipo:
            raise SyntaxError(f"Se esperaba {tipo} y llegó {token.tipo} ({token.valor})")

        self.pos = self.pos + 1

        return token   

    # Analisis para  sumar dos vectores VECTOR(a,b) SUMA VECTOR(a,b) 
    def analisisSintactico(self):

        reservada =  self.consumir("PALABRA").valor.upper()
        self.consumir("IPAREN")
        n1 = float(self.consumir("NUMERO").valor)
        self.consumir("COMA")
        n2 = float(self.consumir("NUMERO").valor)
        self.consumir("DPAREN")

        operacion = self.consumir("PALABRA").valor.upper()

        reservada2 =  self.consumir("PALABRA").valor.upper()

        self.consumir("IPAREN")
        n3 = float(self.consumir("NUMERO").valor)
        self.consumir("COMA")
        n4 = float(self.consumir("NUMERO").valor)
        self.consumir("DPAREN")

        return self.ejecutar(reservada, n1, n2,reservada2, n3, n4,operacion)

    def ejecutar(self, reservada,n1,n2,reservada2, n3, n4,operacion):
        if reservada == "VECTOR" and reservada2 == "VECTOR" and operacion == "SUMA":
            return  (n1+n3, n2+n4)
            


            





