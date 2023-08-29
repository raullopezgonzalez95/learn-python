# imprimir en consola
print("Hola mundo!")

# Variables
variable = "Hola mundo 2"
print(variable)

numero = 28
print(numero)

decimal = 10.5
print(decimal)

boleano = True
print(boleano)

a, b = 3, 4
print(a, b)

# Metodos String
texto = "Hola Mundo"
print(texto.upper())# HOLA MUNDO
print(texto.find("M"))# 5
print(texto.find("Mun"))# se encuentra comenzando en el indice 5
nuevoTexto = texto.replace("Mun", "Raul")# Hola Rauldo
print(texto, nuevoTexto)# Hola Mundo Hola Rauldo
print("Mundo" in texto)# True

# Aritmeticas
print(5 + 15)
print(5 - 15)
print(5 * 15)
print(5 / 15)
print(5 ** 3)# 5 elevado al 3
print(10 % 3)# 1 es el sobrante de la divicion de 10 entre 3

# Comparacion
n1 = 10
n2 = 15
print(n1 > n2)# False
print(n1 < n2)# True
print(n1 <= 10)# True
print(n1 >= 10)# True
print(n2 == 15)# True

# input
edad = input("Ingresa tu edad: ")
print(edad)
print(type(edad))# <class 'str'>

# conversion
print(int(edad) + 10)
