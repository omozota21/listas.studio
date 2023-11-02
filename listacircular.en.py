class Nodo:

    def __init__(self, datos):
        self.datos = datos
        self.siguiente = None

    def printNodo(self):
        print(f"<{self.datos};{self.siguiente}>")

    def __str__(self):
        # return f"<{self.datos};{self.siguiente}>"
        return f"<{self.datos}>"    
