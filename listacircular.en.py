class Nodo:

    def __init__(self, datos):
        self.datos = datos
        self.siguiente = None

    def printNodo(self):
        print(f"<{self.datos};{self.siguiente}>")

    def __str__(self):
        # return f"<{self.datos};{self.siguiente}>"
        return f"<{self.datos}>"    


if __name__ == '__main__':

    n1 = Nodo(11)
    n2 = Nodo(22)
    n3 = Nodo(33)

   
    n1.siguiente = n2
    n2.siguiente = n3
    n3.siguiente = n1

    print(n1)
    print(n2)
    print(n3)

 
    print(n1.siguiente)
    print(n2.siguiente.siguiente)
    print(n3.siguiente.siguiente.siguiente)

    now = n1
    print(now)
    while(now.siguiente):
        now = now.siguiente
        print(now)

    print(n1.siguiente)
    print(n2.siguiente)
    print(n3.siguiente)