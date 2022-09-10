
lista = [1,2,6,8,9]
lista.append(11)
print(lista)

lista.clear()
print(lista)

lista1 = [1,6,9]
lista2 = [6,4,6]
lista1.extend(lista2)
print(lista1)

listaCount = ["Patichoy", "Benavides", "Felipe","juan", "Juan"].count("Juan")
print(listaCount)

listaIndex = ["Juan", "felipe", "benavides","Patichoy", "Juan"].index("benavides")
print(listaIndex)

lista3 = [1,3,5]
lista3.insert(0,0)
lista3.insert(2,2)
lista3.insert(-1,4)
print(lista3)

listaPop = [1,2,3,4,5]
print(listaPop.pop())
print(listaPop.pop(0))
print(listaPop)

listaRemove = [10,20,30,50,60,70,80]
listaRemove.remove(30)
print(listaRemove)

listaRemove.reverse()
print(listaRemove)

listaSort = [1,-30,-35,4,65,-137]
listaSort.sort()
print(listaSort)
listaSort.sort(reverse=True)
print(listaSort)

listaSortAlpa = ["a","b","c","D","H","k"]
listaSorteadatAlpa = sorted(listaSortAlpa, key=str.casefold)
print(listaSorteadatAlpa)
