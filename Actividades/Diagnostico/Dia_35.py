lado1 = input("Introduce el valor del lado 1 del rectángulo: ")
lado2 = input("Introduce el valor del lado 2 del rectángulo: ")

def es_flotante(n, m):
    try:
        float_n = float(n)
        float_m = float(m)
    except ValueError:
        print ("No es un número válido.") 
    else:
        perimetro = 2 * (float_n + float_m) 
        area = float_n * float_m 
        print("El perímetro del rectángulo es", perimetro)
        print("El área del rectángulo es", area)
        
es_flotante(lado1, lado2)