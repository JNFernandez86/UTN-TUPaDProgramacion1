#Alumno: Jorge Nahuel Fernandez
#Materia: Programación 1
#Comisión: M26-C14

#TP Examen 1 - Gestión de Inventario

#Inicialización de listas para almacenar herramientas y existencias, y una variable para contar la cantidad de herramientas.
herramientas = []
existencias = []
cantidad_herramientas=0

# Menú de opciones
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
opcion = input("\nIngrese la opción deseada: ") # Validación de la opción ingresada
opcion.replace(" ","") # Elimina los espacios en blanco de la opción ingresada para evitar errores de validación.
#El programa se ejecutará mientras la opción ingresada no sea un número entero o no esté dentro del rango de opciones válidas (1 a 8). Si la opción es inválida, se mostrará un mensaje de error y se volverá a mostrar el menú hasta que se ingrese una opción válida.
while (opcion.isdigit() == False or int(opcion) < 1 or int(opcion) >= 8):
    if(opcion.isdigit() == False):
        print("\n¡ERROR, No ha ingresado un número entero o ha se encuentra vacia!")
    else:
        print("\n¡ERROR! No ha ingresado ninguna opción...")
    
    #Después de mostrar el mensaje de error, se vuelve a mostrar el menú de opciones para que el usuario pueda ingresar una nueva opción. 
    #El proceso se repetirá hasta que se ingrese una opción válida.  
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
opcion = int(opcion)

#El programa se ejecutará mientras la opción ingresada no sea 8 (Salir). 
#Dentro del bucle, se utilizará una estructura de control "match" para ejecutar diferentes bloques de código según la opción seleccionada por el usuario.
while int(opcion) != 8:
    match opcion:
        case 1: #Carga inicial de herramientas
            print(f"\n{'<' * 10} Carga inicial de herramientas {'>' * 10}\n")
            if len(herramientas) <= 0:#Si no hay herramientas cargadas, se solicitará al usuario que ingrese la cantidad de herramientas que se pondrán a la venta. 
                            
                cantidad_herramientas = input("Ingrese la cantidad de herramientas que se pondran a la venta: ")
                while cantidad_herramientas.isdigit() == False:#Validación de que la cantidad ingresada sea un número entero. 
                    print("\n¡ERROR, No ha ingresado un número entero!")
                    cantidad_herramientas = input("\nvuelva a ingresar la cantidad de herramientas que se pondran a la venta: ")
                #Si la cantidad ingresada es válida, se procederá a solicitar al usuario que ingrese el nombre de cada herramienta.   
                for tools in range(int(cantidad_herramientas)):
                    while True: #Validación de que el nombre de la herramienta no esté vacío y no se encuentre duplicada en la lista de herramientas. 
                        herramienta = input("\nIngrese el nombre de la herramienta: ").capitalize().strip()
                        if not herramienta.replace(" ",""):
                            print("\nEl nombre de la herramienta no puede estar vacía. Por favor, ingrese un nombre válido.")
                            continue
                        if herramienta in herramientas:
                            print(f"\nLa herramienta {herramienta} se encuentra duplicada. ")
                            continue
                #Si el nombre de la herramienta es válido, se agregará a la lista de herramientas utilizando el método "insert" para colocarla en la posición correspondiente
                # según el número de herramientas ingresadas.
                        herramientas.insert(tools,herramienta) 
                        print(f"\n¡La herramienta {herramienta} ha sido ingresada!")
                        break
            else:
                #Si ya hay herramientas cargadas, se mostrará un mensaje indicando que ya existen productos cargados 
                #y se sugerirá al usuario que elija la opción 6 para ingresar nuevos productos.
                print("Ya existen productos cargados, por favor de elegir la opcion 6 para nuevos ingresos")
        case 2:
            #Carga de existencias
            print(f"\n{'<' * 10} Carga de existencias {'>' * 10}\n")
            #Si la cantidad de herramientas es diferente a la cantidad de existencias, 
            #se procederá a solicitar al usuario que ingrese la cantidad de existencias para cada herramienta.
            if len(herramientas) != len(existencias) and len(herramientas) != 0: 
                
                for stock in range(int(cantidad_herramientas)):
                    while True: #Validación de que la cantidad ingresada sea un número entero.
                        cantidad = input(f"\nIngrese la cantidad de existencias del producto {herramientas[stock]}: ")
                        if cantidad.isdigit() == False:#Validación de que la cantidad ingresada sea un número entero. 
                            print("\n¡ERROR, No ha ingresado un número entero!") 
                            continue
                        #Si la cantidad ingresada es válida, se agregará a la lista de existencias utilizando el método "insert" para colocarla en la posición correspondiente
                        #según el número de herramientas ingresadas.
                        existencias.insert(stock,int(cantidad))
                        print(f"\n¡La herramienta {herramientas[stock]} con {cantidad} unidades ha sido ingresada!")
                        break
            elif len(herramientas) <= 0:                  
                    #Si no hay herramientas cargadas, se mostrará un mensaje indicando que no hay herramientas cargadas inicialmente 
                    print("No hay herramientas cargadas inicialmente.")
                    continue
            else:
                #Si la cantidad de herramientas es igual a la cantidad de existencias, se mostrará un mensaje indicando que ya existen productos cargados 
                #y se sugerirá al usuario que elija la opción 6 para ingresar nuevos productos.
                print("Ya existen productos cargados, por favor de elegir la opcion 6 para nuevos ingresos")
        case 3:
            #Visualización de inventario
            print(f"\n{'<' * 10} Visualizacion de inventario {'>' * 10}")
            #Si no hay herramientas cargadas, se mostrará un mensaje indicando que el inventario se encuentra vacío 
            #y se sugerirá al usuario que cargue los productos.
            if len(herramientas)==0:
                print("\n El inventario se encuentra vacío. cargue los productos.")
            #Si no hay existencias cargadas, se mostrará un mensaje indicando que no están cargadas las cantidades de las herramientas
            elif len(existencias)==0:
                print("\nNo estan cargadas las cantidades de las herramientas")
            else:
            #Se recorrerá la lista de herramientas utilizando un bucle "for" 
            #y se mostrará el nombre de cada herramienta junto con su cantidad de existencias correspondiente.
                for herramienta in range(len(herramientas)):
                    print(f"{herramientas[herramienta]}: {existencias[herramienta]} unidades disponibles\n--------------------------------------------")
        case 4:
            #Consulta de Stock
            print(f"\n{'<' * 10} Consulta de Stock {'>' * 10}\n")
            if(len(herramientas)==0):
                #Si no hay herramientas cargadas, se mostrará un mensaje indicando que el inventario se encuentra vacío 
                #y se sugerirá al usuario que cargue los productos.
                print("El inventario se encuentra vacío. Cargue los productos.")
            else:
            #Se solicitará al usuario que ingrese el nombre de la herramienta que desea consultar.
                herramienta_consulta = input("\nIngrese el nombre de la herramienta que desea consultar: ").capitalize().strip()
                #Validación de que el nombre de la herramienta no esté vacío.
                #Si el nombre ingresado es válido, se verificará si la herramienta se encuentra en la lista de herramientas.
                if herramienta_consulta in herramientas:
                    i = herramientas.index(herramienta_consulta)
                    print(f"\n{herramientas[i]}: {existencias[i]} unidades disponibles")
                else:
                    print(f"\nLa herramienta {herramienta_consulta} no se encuentra en el inventario.")
        case 5:
            #Reporte Agotados
            print(f"\n{'<' * 10} Reporte Agotados {'>' * 10}\n")
            if(len(herramientas)==0):
                #Si no hay herramientas cargadas, se mostrará un mensaje indicando que el inventario se encuentra vacío 
                #y se sugerirá al usuario que cargue los productos.
                print("El inventario se encuentra vacío. Cargue los productos.")
            else:
            #Se recorrerá la lista de herramientas utilizando un bucle "for" y se verificará si la cantidad de existencias de cada herramienta es igual a cero.
                for herramienta in range(len(herramientas)):
                    contador_agotados=0
                    if existencias[herramienta] == 0:
                        #Si la cantidad de existencias es igual a cero, se mostrará el nombre de la herramienta indicando que está agotada.
                        print(f"\n{herramientas[herramienta]}: Agotado")
                        contador_agotados += 1
                if contador_agotados == 0:
                    #Si no hay herramientas agotadas, se mostrará un mensaje indicando que no hay herramientas agotadas en el inventario.
                    print("\nNo hay herramientas agotadas en el inventario.")
        
        case 6:
            #Alta nuevo producto
            print(f"\n{'<' * 10} Alta de nuevo producto {'>' * 10}\n")
            #Se solicitará al usuario que ingrese el nombre de la herramienta que desea agregar.
            while True:
                    #Validación de que el nombre de la herramienta no esté vacío y no se encuentre duplicada en la lista de herramientas.
                    herramienta = input("\nIngrese el nombre de la herramienta que desea agregar: ").capitalize().strip()
                    if not herramienta.replace(" ",""):
                        print("\nEl nombre de la herramienta no puede estar vacía. Por favor, ingrese un nombre válido.")
                        continue
                    if herramienta in herramientas:
                        print(f"\nLa herramienta {herramienta} se encuentra duplicada. ")
                        continue
                    #Si el nombre de la herramienta es válido, se solicitará al usuario que ingrese la cantidad de existencias para esa herramienta.
                    cantidad = input(f"\nIngrese la cantidad de existencias del producto herramienta: ")
                    #Validación de que la cantidad ingresada sea un número entero.
                    while True:
                        if cantidad.isdigit() == False:
                            print("\n¡ERROR, No ha ingresado un número entero ") 
                            cantidad = input(f"\nIngrese la cantidad de existencias del producto herramienta: ")
                            continue
                        else:
                            break
                    #Si la cantidad ingresada es válida, se agregará el nombre de la herramienta a la lista de herramientas 
                    #y la cantidad de existencias a la lista de existencias utilizando el método "append" para agregarlo al final de cada lista.
                    herramientas.append(herramienta) 
                    existencias.append(int(cantidad))
                    #Se mostrará un mensaje indicando que la herramienta con la cantidad de unidades ha sido ingresada correctamente.
                    print(f"\n¡La herramienta {herramienta} con {cantidad} unidades ha sido ingresada!")
                    break
            print()
        case 7:
            #Actualización de Stock (Venta/Ingreso)
            print(f"\n{'<' * 10} Actualización de Stock (Venta/Ingreso) {'>' * 10}")
            #Se solicitará al usuario que elija si desea realizar una venta o un ingreso de stock.
            actualizacion_stock = input("Elija 1 para Venta o 2 para Ingreso: ")
            #Validación de que la opción ingresada sea un número entero y esté dentro del rango de opciones válidas (1 o 2). 
            #Si la opción es inválida, se mostrará un mensaje de error y se volverá a solicitar la opción hasta que se ingrese una opción válida.
            while actualizacion_stock.isdigit() == False or int(actualizacion_stock) < 1 or int(actualizacion_stock) > 2:
                #Si la opción ingresada no es un número entero, se mostrará un mensaje de error indicando que no se ha ingresado un número entero.
                if actualizacion_stock.isdigit() == False:
                    print("\n¡ERROR, No ha ingresado un número entero!")
                else:
                    print("\n¡ERROR, No ha ingresado la opción válida!")
                actualizacion_stock = input("\nElija 1 para Venta o 2 para Ingreso: ")
            #Si la opción ingresada es válida, se procederá a realizar la actualización de stock según la opción seleccionada (venta o ingreso).    
            if int(actualizacion_stock) == 1:
                #Si el usuario elige la opción de venta, se solicitará que ingrese el nombre de la herramienta que desea vender 
                # y la cantidad de unidades que desea vender.
                print(f"{'<' * 20} Venta {'>' * 20}")
                venta_herramienta = input("Ingrese la herramienta que desea vender: ").capitalize().strip()
                #Validación de que el nombre de la herramienta no esté vacío y se encuentre en la lista de herramientas.
                if not venta_herramienta.replace(" ",""):
                    print("\nEl nombre de la herramienta no puede estar vacía. Por favor, ingrese un nombre válido.")
                    continue
                if venta_herramienta not in herramientas:
                    print(f"\nLa herramienta {venta_herramienta} no se encuentra cargada, por favor de ingresar una herramienta válida ")
                    continue
                #Si el nombre de la herramienta es válido, se solicitará al usuario que ingrese la cantidad de unidades que desea vender.
                cantidad_venta = input(f"ingrese la cantidad de venta de la herramienta {venta_herramienta}: ")
                #Validación de que la cantidad ingresada sea un número entero y mayor a cero. Si la cantidad es inválida, se mostrará un mensaje de error 
                #y se volverá a solicitar la cantidad hasta que se ingrese una cantidad válida.
                if cantidad_venta.isdigit() == False or int(cantidad_venta) < 0:
                    print("\n¡ERROR, No ha ingresado un número entero ") 
                    continue
                #Si la cantidad ingresada es válida, se verificará si hay suficiente stock disponible para realizar la venta.
                if venta_herramienta in herramientas:
                    cantidad = herramientas.index(venta_herramienta)
                #Si la cantidad de unidades que se desea vender es menor o igual a la cantidad de existencias disponibles para esa herramienta,
                #se realizará la venta restando la cantidad vendida del stock actual.
                if int(cantidad_venta) <= int(existencias[cantidad]) and int(cantidad_venta) > 0:
                    stock_actualizado = int(existencias[cantidad]) - int(cantidad_venta)
                    existencias[cantidad] = stock_actualizado
                    print(f"\n¡Se ha realizado la venta correctamente de la herramienta {venta_herramienta} de {cantidad_venta} unidades!\n")
                    #Si la cantidad de unidades que se desea vender es mayor a la cantidad de existencias disponibles para esa herramienta,
                    # Se mostrará un mensaje indicando que no hay suficiente stock para realizar la venta y se sugerirá al usuario que intente nuevamente.
                else:
                    print(f"\n¡No hay suficiente stock para vender {cantidad_venta} unidades de {venta_herramienta}!\n")
                    print("¡Intente nuevamente!")
                    continue
            else:
                #Si el usuario elige la opción de ingreso, se solicitará que ingrese el nombre de la herramienta para la cual desea aumentar el stock 
                #y la cantidad de unidades que desea agregar al stock.
                print(f"{'<' * 20} Compra {'>' * 20}")
                compra_herramienta = input("Ingrese el producto a aumentar el stock: ").capitalize().strip()
                #Validación de que el nombre de la herramienta no esté vacío y se encuentre en la lista de herramientas. 
                #Si el nombre es inválido, se mostrará un mensaje de error
                if not compra_herramienta.replace(" ",""):
                    print("\nEl nombre de la herramienta no puede estar vacía. Por favor, ingrese un nombre válido.")
                    continue
                if compra_herramienta not in herramientas:
                    print(f"\nLa herramienta {compra_herramienta} no se encuentra cargada, por favor de ingresar una herramienta válida ")
                    continue
                #Si el nombre de la herramienta es válido, se solicitará al usuario que ingrese la cantidad de unidades que desea agregar al stock.
                cantidad_venta = input(f"ingrese la cantidad de venta de la herramienta {compra_herramienta}: ")
                if cantidad_venta.isdigit() == False or int(cantidad_venta) < 0:
                    print("\n¡ERROR, No ha ingresado un número entero ") 
                    continue
                #Si la cantidad ingresada es válida, se actualizará el stock sumando la cantidad ingresada al stock actual de esa herramienta.
                if compra_herramienta in herramientas:
                    cantidad = herramientas.index(compra_herramienta)
                    stock_actualizado = int(existencias[cantidad]) + int(cantidad_venta)
                    existencias[cantidad] = stock_actualizado
                    print(f"\n¡Se ha realizado la compra correctamente de la herramienta {compra_herramienta} de {cantidad_venta} unidades!\n")
                #Si la cantidad ingresada es válida, se actualizará el stock sumando la cantidad ingresada al stock actual de esa herramienta.
                else:
                    print(f"\nLa herramienta {compra_herramienta} no se encuentra cargada, por favor de ingresar una herramienta válida ")
                    continue
    #Después de ejecutar la opción seleccionada, se mostrará nuevamente el menú de opciones para que el usuario pueda elegir otra opción o salir del programa.

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
    opcion = input("\nQuiere realizar otra opción?: ")
    opcion = int(opcion)
#Cuando el usuario elige la opción de salir (opción 8), se mostrará un mensaje de despedida.
print("\nGracias por utilizar el programa de gestión de inventario. ¡Hasta luego!")
input("\nPresione Enter para salir... ")