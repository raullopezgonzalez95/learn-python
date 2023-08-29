# Listas
lista_de_numeros = [1, 2, 3, 4, 5]
#                   0, 1, 2, 3, 4
#print(lista_de_numeros[1])

lista_de_numeros_2 = []
lista_de_numeros_2.append(1)
lista_de_numeros_2.append(2)
lista_de_numeros_2.append(3)
#print(lista_de_numeros_2[0])

lista = []
lista.append(10 + 10)
lista.append("hola mundo")
lista.append(30 / 5)
lista.append([1, 2, 3, 4, 5])
lista.append(True)


for numero in lista:
    print("el valor:", numero, "es de tipo:", type(numero))
    print("--------------------------------------------------------------------")
