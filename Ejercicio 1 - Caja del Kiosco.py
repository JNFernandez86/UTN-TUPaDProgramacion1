#### DECLARACION DE VARIABLES E INICIACION DE CONTADORES
suma_precios = 0
descuento_producto=0.0
promedio_productos = 0
monto_descontado =0 
ahorro=0


nombre_cliente = input("Ingrese el nombre del cliente: ").capitalize()
#### Validaciones con Bucle While ####
while(nombre_cliente.isalpha() == False or nombre_cliente ==""): # Validación de si es una letra y que el nombre no este vacio
    print("\nNo ha ingresado el nombre del cliente correctamente o se encuentra vacío")
    nombre_cliente = input("\nIngrese el nombre del cliente: ").capitalize()

cantidad_productos = input("\nIngrese la cantidad de productos: ")
while(cantidad_productos.isdigit()== False or cantidad_productos == "0"): # Validacion de que no sea menor a 0(el negativo lo toma como cáracter) y que contenga solo numero.
    print("\nHa ingresado un caracter incorrecto o ha ingresado 0 (Solo se permiten Números enteros)\n")
    cantidad_productos = input("Reingrese la cantidad de productos: ")

#### Ingreso de Productos dependientes del numero ingresado  ####
for x in range(int(cantidad_productos)):
    precio=input("\nIngrese Precio sin decimales: " )
    while(precio.isdigit()==False): # Validacion de numero entero
        print("Ha ingresado un caracter incorrecto (Solo se permiten Números enteros)\n")
        print("Reingrese el precio")
    respuesta_descuento = input("\nEl Producto, posee descuentos? S/N: ").upper()
    while(respuesta_descuento != 'S' and respuesta_descuento!="N"): # Validación de respuesta. para n, N, s y S
        print("Ha ingresado una opcion errónea. ingrese S=Sí N=No)\n")
        respuesta_descuento = input("El Producto, posee descuentos? S/N: ").upper()
    if(respuesta_descuento == 'S'):
        descuento_producto = float(int(precio) * 0.1)
    suma_precios += int(precio) # Acumulador de los precios
    ahorro += float(descuento_producto) #Acumulador de los descuentos
    
#### CÁLCULOS TOTALES #####

promedio_productos = float(suma_precios / int(cantidad_productos))
monto_descontado = float(suma_precios-ahorro)

#### SALIDAS ####
print("\n#################################################")
print(f"\nCliente: {nombre_cliente}")
print(f"\nCantidad de productos ingresados: {cantidad_productos}")
print(f"\nMONTO TOTAL DE LA COMPRA: ${suma_precios} (Sin Descuentos)")
print(f"MONTO TOTAL a pagar: ${monto_descontado:.2f} (con descuentos)")
print(f"AHORRO: ${ahorro:.2f}")
print(f"El promedio por producto es: ${promedio_productos:.2f}\n")