'''Escribir un programa que pregunte al usuario por las ventas de un rango de años y 
muestre por pantalla una serie con los datos de las ventas indexada por los años, antes y después de aplicarles un descuento del 10%.'''
# Pedir al usuario el rango de años
inicio = int(input("Ingrese el año de inicio: "))
fin = int(input("Ingrese el año de fin: "))

# Crear un diccionario para almacenar las ventas por año
ventas = {}

# Iterar sobre el rango de años
for año in range(inicio, fin + 1):
    # Pedir al usuario las ventas para el año actual
    ventas_año = float(input(f"Ingrese las ventas para el año {año}: "))
    
    # Aplicar el descuento del 10%
    ventas_descuento = ventas_año * 0.9
    
    # Almacenar las ventas en el diccionario
    ventas[año] = ventas_descuento

# Mostrar las ventas indexadas por año
for año, ventas_año in ventas.items():
    print(f"Ventas para el año {año}: {ventas_año}")
