class Token:
    def __init__(self, tipo, valor):
        self.tipo = tipo # Tipo Dato
        self.valor = valor # Contenido
    
    # Metodo para convertir un objeto en json
    def to_json(self):
        return self.__dict__ 

    # Representacion formal del objeto a la hora de imprimir
    def __repr__(self):
        return f"{self.tipo}, {self.valor!r}"