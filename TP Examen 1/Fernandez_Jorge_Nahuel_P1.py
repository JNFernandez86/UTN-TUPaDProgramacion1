#

herramientas = []
existencias = []
cantidad_herramientas=0

print("\n<<<<<<<<<<<<<<< Menú de Opciones >>>>>>>>>>>>>>>\n")
print("1: Carga inicial de herramientas")
print("2: Carga de existencias")
print("3: Visualizacion de inventario")
print("4: Consulta de Stock")
print("5: Reporte Agotados")
print("6: Alta nuevo producto")
print("7: Actualización de Stock (Venta/Ingreso)")
print("8: Salir")
print("____________________________________________")
opcion = input("\nIngrese la opción deseada: ")

while (opcion.isdigit() == False or int(opcion) < 0 or int(opcion) >= 8):
    if(opcion.isdigit() == False):
        print("\n¡ERROR, No ha ingresado un número entero!")
        
    else:
        print("\n¡ERROR, No ha ingresado la opción válida!")

    input("\nPresione Enter para mostrar nuevamente el menú... ")
    print("\n<<<<<<<<<<<<<<< Menú de Opciones >>>>>>>>>>>>>>>\n")
    print("1: Carga inicial de herramientas")
    print("2: Carga de existencias")
    print("3: Visualizacion de inventario")
    print("4: Consulta de Stock")
    print("5: Reporte Agotados")
    print("6: Alta nuevo producto")
    print("7: Actualización de Stock (Venta/Ingreso)")
    print("8: Salir")
    print("____________________________________________")
    opcion = input("\nIngrese la opción deseada: ")
while int(opcion) != 8:

    match int(opcion):
        case 1:
            cantidad_herramientas = input("Ingrese la cantidad de herramientas que se pondran a la venta: ")
            while cantidad_herramientas.isdigit() == False:
                print("¡ERROR, No ha ingresado un número entero!")
                cantidad_herramientas = input("vuelva a ingresar la cantidad de herramientas que se pondran a la venta: ")
            for tools in range(int(cantidad_herramientas)):
                herramienta = input("Ingrese el nombre de la herramienta: ")
                herramientas.append(herramienta)
                
        case 2:
            for stock in range(int(cantidad_herramientas)):
                cantidad = input(f"Ingrese la cantidad de existencias del producto {herramientas[stock]}: ")
                existencias.append(cantidad)
            
        case 3:
            print()
        case 4:
            print()
        case 5:
            print()
        case 6:
            print()
        case 7:
            print()
        case 8:
            break
    opcion = input("\nDesea realizar otra operacion?: ")


print("Adios")
#print(herramientas,stock)