def es_flotante(n):
    try:
        float_n = float(n)
    except ValueError:
        print ("No es un número válido.")    
    else:
        perimetro = 4 * float (lado)
        area = float (lado) ** 2
        print("El perímetro del cuadrado es", perimetro)
        print("El área del cuadrado es", area)

lado = input("Introduce el valor del lado del cuadrado: ")

es_flotante(lado)
