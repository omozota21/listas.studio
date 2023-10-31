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

    def insertar(self, nuevo_nodo):
        if not self.head: # sera el 1er nodo:
            ## asignar el nodo a la cabeza
            self.head = nuevo_nodo
        else:
            ## obtener el ultimo_nodo
            ultimo = self.head
            while ultimo != None:
                ultimo = ultimo.siguiente
            ## asignar el nuevo nodo al puntero siguiente del último nodo
            ultimo.siguiente = nuevo_nodo            

    def printLES(self):
        if self.head:
            print(self.head.printNodo())
            ultimo = self.head            
            while ultimo != None:
                ultimo = ultimo.siguiente                
                ultimo.printNodo()

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

    # print(n1) # ok, existe __str__()
    # print(n2) # ok, existe __str__()   

    # Cosa similar: serialización -marshalling- (similar!!)
    # https://es.wikipedia.org/wiki/Serializaci%C3%B3n)


    LES = ListaEnlazadaSimple()
    LES.printLES()

    LES.insertar(n2)  ## ramon
    LES.printLES()

    LES.insertar(n1)  ## 11
    LES.printLES()




