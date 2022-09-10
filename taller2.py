# append() Añade un ítem al final de la lista:
lista = [1,2,6,8,9]
lista.append(11)
print(lista)
# clear() Vacía todos los ítems de una lista:
lista.clear()
print(lista)
# extend() Une una lista a otra:
lista1 = [1,6,9]
lista2 = [6,4,6]
lista1.extend(lista2)
print(lista1)
# count() Cuenta el número de veces que aparece un ítem:
listaCount = ["Patichoy", "Benavides", "Felipe","juan", "Juan"].count("Juan")
print(listaCount)
# index() Devuelve el índice en el que aparece un ítem (error si no aparece):
listaIndex = ["Juan", "felipe", "benavides","Patichoy", "Juan"].index("benavides")
print(listaIndex)
# insert() Agrega un ítem a la lista en un índice específico
lista3 = [1,3,5]
lista3.insert(0,0)
lista3.insert(2,2)
lista3.insert(-1,4)
print(lista3)
# pop() Extrae un ítem de la lista y lo borra:
listaPop = [1,2,3,4,5]
print(listaPop.pop())
print(listaPop.pop(0))
print(listaPop)
# remove() Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos:
listaRemove = [10,20,30,50,60,70,80]
listaRemove.remove(30)
print(listaRemove)
# reverse() Le da la vuelta a la lista actual:
listaRemove.reverse()
print(listaRemove)
# sort() Ordena automáticamente los ítems de una lista por su valor de menor a mayor:
listaSort = [1,-30,-35,4,65,-137]
listaSort.sort()
print(listaSort)
listaSort.sort(reverse=True)
print(listaSort)
# Ejercicio Casa
listaSortAlpa = ["a","b","c","D","H","k"]
listaSorteadatAlpa = sorted(listaSortAlpa, key=str.casefold)
print(listaSorteadatAlpa)
