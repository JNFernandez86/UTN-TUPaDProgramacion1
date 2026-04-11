# # Listas Ejercicio 2

lista_productos=[]

#ingreso de los 5 productos a la lista de productos
for producto in range(5):
    nombre_producto = input("Ingrese el producto a cargar: ").capitalize()
    lista_productos.append(nombre_producto) 

#Productos ordenados alfabeticamente
productos_ordenados = sorted(lista_productos)
print("\n######### Ordenados alfabeticamente ##########\n")
for x in range(len(productos_ordenados)):
    print(f"Producto {x+1}: {productos_ordenados[x]}")

#Solicitud de producto a eliminar
eliminar_producto = input("\nIngrese el producto que desea eliminar: ").capitalize()

#Búsqueda en la lista del producto ingresado por el usuario.
if eliminar_producto in lista_productos:
    lista_productos.remove(eliminar_producto)
    print("El producto ha sido eliminado...\n")
else:
    print("No se ha encontrado el item a eliminar... \n")  

#Actualización de la lista.
print("<<<<<<<<<< Lista actualizada >>>>>>>>>>\n")
for x in range(len(lista_productos)):
    print(f"Producto {x+1}: {lista_productos[x]} ")

input("\nPresione Enter para terminar")