import numpy as np

def operaciones(A, B):
    suma = np.add(A, B)
    resta = np.subtract(A, B)
    multiplicacion = np.multiply(A, B)
    division = np.divide(A, B)

    print("Suma", suma)
    print("Resta", resta)
    print("Multiplicacion", multiplicacion)
    print("Division", division)

