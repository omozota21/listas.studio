## pregunta

Dame un código python orientado a objeto para una lista enlazada simple que contenga nodos con un dato también simple y que tenga las clases con los nombres NodoSimple y ListaEnlazadaSimple respectivamente.

## respuesta

```python
class NodoSimple:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazadaSimple:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None

    def agregar_elemento(self, dato):
        nuevo_nodo = NodoSimple(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar_elemento(self, dato):
        if self.esta_vacia():
            return

        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            return

        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.dato == dato:
                actual.siguiente = actual.siguiente.siguiente
                return
            actual = actual.siguiente

    def mostrar(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos

# Ejemplo de uso:
mi_lista = ListaEnlazadaSimple()
mi_lista.agregar_elemento(1)
mi_lista.agregar_elemento(2)
mi_lista.agregar_elemento(3)

print("Elementos en la lista:", mi_lista.mostrar())

mi_lista.eliminar_elemento(2)
print("Elementos en la lista después de eliminar 2:", mi_lista.mostrar())

```
