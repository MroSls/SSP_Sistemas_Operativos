base = float(input("Introduce el valor de la base del triángulo: "))
altura = float(input("Introduce el valor de la altura del triángulo: "))

def es_flotante(n, m):
    try:
        float_n = float(n)
        float_m = float(m)
    except ValueError:
        print ("No es un número válido.") 
    else:
        area = 0.5 * float_n * float_m 
        print("El área del triángulo es", area, ".")
        
es_flotante(base, altura)