class Nodo:

    def __init__(self, datos):
        self.datos = datos
        self.siguiente = None

    def printNodo(self):
        print(f"<{self.datos};{self.siguiente}>")

    def __str__(self):
        # return f"<{self.datos};{self.siguiente}>"
        return f"<{self.datos}>"    

class ListaEnlazadaSimple:
    def __init__(self):
        self.head = None

if __name__ == '__main__':

    n1 = Nodo(11)
    n2 = Nodo("ramon")

    # impresion...
    # 1. sin un servicio del objeto
    # print(n1.datos)
    # print(n1.siguiente)
    # print(n1) # sale repr()
    # print(n2) # sale repr()

    # print(n2.datos)
    # print(n2.siguiente)

    # 2. con un servicio del objeto
    # n1.printNodo()
    # n2.printNodo()

    # 3. con la expresion del objeto como string: str() ... repr()
    # https://www.digitalocean.com/community/tutorials/python-str-repr-functions  

    print(n1) # ok, existe __str__()
    print(n2) # ok, existe __str__()   

    # Cosa similar: serialización -marshalling- (similar!!)
    # https://es.wikipedia.org/wiki/Serializaci%C3%B3n)


