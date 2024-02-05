a = input("Introduce el valor del lado a del triángulo: ")
b = input("Introduce el valor del lado b del triángulo: ")
c = input("Introduce el valor del lado c del triángulo: ")

def validarTriangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        perimetro = a + b + c
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print("El perímetro del triángulo es", perimetro)
        print("El área del triángulo es", area)
    else:
        print("Los valores ingresados no corresponden a un triángulo.")

def es_flotante(n, m, o):
    try:
        float_n = float(n)
        float_m = float(m)
        float_o = float(o)
    except ValueError:
        print ("No es un número válido.") 
    else:
        validarTriangulo(float_n, float_m, float_o)
        
es_flotante(a, b, c)
