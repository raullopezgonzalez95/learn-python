lista_calificaciones = [55, 71, 46, 87, 55]

suma_total = 0
for calificacion in lista_calificaciones:
    suma_total = suma_total + calificacion

promedio = suma_total / len(lista_calificaciones)

print("El promedio es:", promedio)
# El promedio es: 64.75
