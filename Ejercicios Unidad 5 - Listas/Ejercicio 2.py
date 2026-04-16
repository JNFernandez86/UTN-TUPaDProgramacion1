# # Listas Ejercicio 2

# Lista que almacenará los productos ingresados por el usuario
lista_productos = []

# Carga de 5 productos: .capitalize() asegura que cada nombre empiece con mayúscula
for producto in range(5):
    nombre_producto = input("Ingrese el producto a cargar: ").capitalize()
    lista_productos.append(nombre_producto)

# sorted() devuelve una nueva lista ordenada alfabéticamente sin modificar la original
productos_ordenados = sorted(lista_productos)

print("\n######### Ordenados alfabéticamente ##########\n")
for x in range(len(productos_ordenados)):
    print(f"Producto {x+1}: {productos_ordenados[x]}")

# Se solicita al usuario el producto que desea eliminar
# .capitalize() para que la comparación sea consistente con cómo fueron guardados
eliminar_producto = input("\nIngrese el producto que desea eliminar: ").capitalize()

# Se verifica si el producto existe en la lista original
# .remove() elimina la primera aparición del valor encontrado
if eliminar_producto in lista_productos:
    lista_productos.remove(eliminar_producto)
    print("El producto ha sido eliminado...\n")
else:
    print("No se ha encontrado el ítem a eliminar...\n")

# Se muestra la lista original actualizada tras la eliminación
print("<<<<<<<<<< Lista actualizada >>>>>>>>>>\n")
for x in range(len(lista_productos)):
    print(f"Producto {x+1}: {lista_productos[x]}")

# Pausa para que el usuario pueda leer los resultados antes de cerrar
input("\nPresione Enter para terminar")