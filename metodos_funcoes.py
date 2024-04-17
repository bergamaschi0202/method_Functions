import os
os.system('cls')

print("lista")
l= ["edson", 12, 1.67, True, 34]

print(f" 1 posição da lista: L[1] = {l[1]}")
print(f"lista inteira: L = {l}")

l[4] = "edson"
print(f"L = {l}")
print("-------------------------------")

print("append")

lista= list()
print(f"lista = {lista}")
lista.append(22)
lista.append("logica")
print(f"lista = {lista}")
print("-------------------------------")

print("insert")
lista= [22,"logica"]
print(f"lista = {lista}")
lista.insert(1, 57.7)
print(f"lista = {lista}")
print("-------------------------------")

print("pop")
lista= [22, 57.7, "logica"]
print(f"lista = {lista}")
lista.pop(0)
print(f"lista = {lista} ")
lista.pop()
print(f"lista = {lista}")
print("-------------------------------")

print("remove")
lista=[22, 57.7, "logica"]
print(f"lista = {lista}")
lista.remove(57.7)
print(f"lista = {lista}")
print("-------------------------------")

print("index")
lista=[22, 57.7, "logica","fefanoffe"]
print(f"lista = {lista}")
indice= lista.index("logica")
print(f"indice: {indice}")
indice= lista.index("fefanoffe")
print(f"indice: {indice}")
print("-------------------------------")

print("count")
lista= [22,22, 57.7, "logica"]
print(f"lista = {lista}")
qtd= lista.count(30)
print(f"quantidade = {qtd}")
print("-------------------------------")

print("len")
lista= [22,22, 57.7, "logica"]
print(f"lista = {lista}")
qtd_elementos= len(lista)
print(f"quantidade = {qtd_elementos}")
print("-------------------------------")

print("sum")
lista =[19,4,25,33,-5]
print(f"lista = {lista}")

print(sum(lista))
print("-------------------------------")

print("+")
lista1 =[1,2,3]
print(f"lista 1 = {lista1}")
lista2 =[4,5,6]
print(f"lista 2 = {lista2}")

lista3= lista1 + lista2
print(f"lista 3 = {lista3}")
lista3= lista2 + lista1
print(f"lista 4 = {lista3}")
lista2= lista1 + lista2
print(f"lista 5 = {lista2}")
print("-------------------------------")

print("extend")
lista1 =[1,2,3]
print(f"lista 1 = {lista1}")
lista2 =[4,5,6]
print(f"lista 2 = {lista2}")
lista2.extend(lista1)
print(f"lista = {lista2}")
print("-------------------------------")

print("copy")
lista1 =[1,2,3]
print(f"lista = {lista}")
lista2 = lista1.copy()
print(f"lista 1 = {lista1}")
print(f"lista 2 = {lista2}")
print("-------------------------------")

print("sort")
lista = [19,4,25,33,-5]
print(f"lista = {lista}")
lista.sort()
print(f"lista sort = {lista}")

lista.sort(reverse=True)
print(f"lista sort reverse = {lista}")
print("-------------------------------")

print("reverse")
lista = [19,4,25,33,-5]
print(f"lista = {lista}")
lista.reverse()
print(f"lista = {lista}")
print("-------------------------------")

print("clear")
lista = [19,4,25,33,-5]
print(f"lista = {lista}")
lista.clear()
print(f"lista = {lista}")
print("-------------------------------")

print("del")
lista = [19,4,25,33,-5]
del(lista)
print("-------------------------------")