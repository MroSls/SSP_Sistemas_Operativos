import Practica1_1

filas = int(input("Ingresa el número de filas: "))
columnas = filas

matriz = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        dato = int(input(f"Ingrese el elemento de la matriz 1 en la posición ({i+1}, {j+1}): "))
        fila.append(dato)
    matriz.append(fila)

matriz2 = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        dato = int(input(f"Ingrese el elemento de la matriz 2 en la posición ({i+1}, {j+1}): "))
        fila.append(dato)
    matriz2.append(fila)

print("La matriz 1 es:")
for fila in matriz:
    print(fila)

print("La matriz 2 es:")
for fila in matriz2:
    print(fila)
Practica1_1.operaciones(matriz, matriz2)