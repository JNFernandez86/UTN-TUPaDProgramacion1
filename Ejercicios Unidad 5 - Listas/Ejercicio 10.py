# Ejercicio 10

#Inicializacion de la matriz 4x7
ventas = [
    [12, 15, 22, 18, 20, 25, 20],  # Producto 1
    [ 8, 11, 39, 13, 36, 19, 25],  # Producto 2
    [ 5, 7, 16, 29, 11, 14, 21],   # Producto 3
    [20, 22, 31, 25, 28, 30, 10]   # Producto 4
]
#Lista para reemplazar el indice por el día correspondiente
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
mayor_producto =0

#Suma de totales por cada producto
for producto in range(len(ventas)):
    total = 0
    for dia in range(len(ventas[producto])):
        total += ventas[producto][dia]
#Realiza la obtención del prodicto mas vendido de la semana
        if(total > mayor_producto):
            mayor_producto = total
            maxproducto = producto
    print(f"Producto {producto+1}: $ {total} unidades")
#Cálculo de el día con mayor ventas
venta_mayor=0
j = 0
while j < len(dias):
    total_vendido = 0
    i = 0
    while i < len(ventas):
        total_vendido += ventas[i][j]
        i += 1
    if total_vendido > venta_mayor:
        venta_mayor = total_vendido
        diamax = j
    j += 1

#Resultados
print(f"\nEl dia con mayor venta fue el: {dias[diamax]} con {venta_mayor}\n")
print(f"El producto mas vendido fue el N°{maxproducto+1}\n")


