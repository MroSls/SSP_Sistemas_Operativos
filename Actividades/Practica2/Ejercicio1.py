'''Escribir un programa que pregunte al usuario por las ventas de un rango de años y 
muestre por pantalla una serie con los datos de las ventas indexada por los años, antes y después de aplicarles un descuento del 10%.'''

inicio = int(input("Ingrese el año de inicio: "))
fin = int(input("Ingrese el año de fin: "))
ventas = {}

for año in range(inicio, fin + 1):
    ventas_año = float(input(f"Ingrese las ventas para el año {año}: "))
    ventas_descuento = ventas_año * 0.9
    ventas[año] = ventas_descuento
for año, ventas_año in ventas.items():
    print(f"Ventas para el año {año}: {ventas_año}")
