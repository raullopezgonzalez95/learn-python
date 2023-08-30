a: int = 7
b: int = 5

def pitagoras(a: int, b: int):
    a_cuadrada: int = pow(a, 2)
    b_cuadrada: int = pow(b, 2)
    suma_cuadrados: int = a_cuadrada + b_cuadrada
    c = pow(suma_cuadrados, 1/2)
    return c

print(pitagoras(a, b))