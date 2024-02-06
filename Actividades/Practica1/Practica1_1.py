def operaciones(A, B):
    suma = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
    resta = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
    multiplicacion = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
    division = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            suma[i][j] = A[i][j] + B[i][j]
            resta[i][j] = A[i][j] - B[i][j]
            multiplicacion[i][j] = A[i][j] * B[i][j]
            division[i][j] = A[i][j] / B[i][j]

    print("Suma", suma)
    print("Resta", resta)
    print("Multiplicacion", multiplicacion)
    print("Division", division)