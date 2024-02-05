import numpy as np
import Practica1_2

filas = int(input("Ingresa el número de filas: "))
columnas = filas

matriz = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        dato = int(input(f"Ingrese el elemento en la posición ({i+1}, {j+1}): "))
        fila.append(dato)
    matriz.append(fila)

matriz = np.array(matriz)

matriz2 = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        dato = int(input(f"Ingrese el elemento en la posición ({i+1}, {j+1}): "))
        fila.append(dato)
    matriz2.append(fila)

matriz2 = np.array(matriz)

print("La matriz 1 es:")
print(matriz)
print("La matriz 2 es:")
print(matriz2)

Practica1_2.operaciones(matriz, matriz2)