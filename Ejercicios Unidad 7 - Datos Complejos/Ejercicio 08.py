# 8)

def menu():
    print("\n<<<<< Menú >>>>>>\n")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades al stock")
    print("3. Agregar un nuevo producto")
    print("4. Salir")
    
def solo_numeros(opcion):
    while True:
        if opcion.isdigit() and int(opcion) in [1, 2, 3, 4] :
            return int(opcion)
        else:
            print("Ingrese una opción válida del 1 al 4")
            opcion = input("Ingrese una opción: ")    

def validar_unidades(unidades):
    while True:
        if unidades.isdigit() and int(unidades) > 0:
            return int(unidades)
        else:
            print("Ingrese una cantidad válida de unidades (número entero positivo)")
            unidades = input("Ingrese la cantidad de unidades: ")
    
productos = {'Destornillador':100, 'Alicate':150,'Llave inglesa':30,'Llave francesa': 25, "Llaves Alems":42,
            "Serrucho":65}

while True:
    menu()
    opcion = input("\nIngrese una opción: ")
    opcion = solo_numeros(opcion)

    match(opcion):
        case 1:
            print("\n<<<<< Busquéda de productos >>>>>>")
            buscar_producto = input("Ingrese el producto para consultar stock: ").capitalize()
            if buscar_producto in productos:
                print(f"El producto {buscar_producto} tiene {productos[buscar_producto]} unidades en stock")
            else:
                print("No se ha encontrado el producto buscado")
            
        case 2:
            print("<<<<< Agregar unidades al stock >>>>>>")
            producto_agregar = input("Ingrese el producto para agregar unidades: ").capitalize()
            if producto_agregar in productos:
                unidades_agregar = input("Ingrese la cantidad de unidades a agregar: ")
                unidades_agregar = validar_unidades(unidades_agregar)
                productos[producto_agregar] += unidades_agregar
                print(f"Se han agregado {unidades_agregar} unidades al producto {producto_agregar}. Stock actual: {productos[producto_agregar]} unidades")
            else:
                print("No se ha encontrado el producto para agregar unidades")
            
        case 3:
            print("\n<<<<< Agregar nuevo producto >>>>>>")
            nuevo_producto = input("Ingrese el nombre del nuevo producto: ").capitalize()
            if nuevo_producto not in productos:
                cantidad = input("Ingrese la cantidad de unidades del nuevo producto: ")
                cantidad = validar_unidades(cantidad)
                productos[nuevo_producto] = cantidad
                print(f"Se ha agregado el producto {nuevo_producto} con {cantidad} unidades.")
            else:
                print("El producto ya existe en el inventario.")
        case 4:
            print("¡Gracias por usar el sistema!")
            break
    input("\nPresione Enter para continuar...")
