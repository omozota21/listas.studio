# listas.studio

Estudio de listas como estructuras dinamicas

## Empezamos con python (es mas facil...)

```python
lista = []
lista.append(22)
lista.append(55)
lista.append(11)
print(lista)

lista2 = lista.copy()
print(lista2)

lista2.append("END")
print(lista2)

lista2.clear()
print(lista2)

# INTROSPECCION EN PYTHON
# https://stackoverflow.com/questions/1006169/how-do-i-look-inside-a-python-object

print(dir(lista2))
## try: lista.__dir__
## try: dir(lista)
## try: type(lista)
## try: isistance(lista,list)
```

## listas enlazadas (¿tipo C?) [¿OO?]

Códigos de: [**aqui**](https://geekflare.com/es/python-linked-lists/) 

En una lista enlazada simple cada nodo contiene un -único- puntero conectado al siguiente -nodo- -de la lista enlazada-. 

Para cada nodo de la lista enlazada tenemos que gestionar el dato que contiene y el enlace al -eventual- siguiente nodo.


