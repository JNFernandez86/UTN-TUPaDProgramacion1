# Ejercicio 5

estudiantes = ['Marcos','Pedro','Laura','Lucas','Jorge','Milagros','Nahuel','Abel']

opcion = input("\n_MENU_\n1. Quiere agregar un nuevo estudiante\n2. Desea eliminar un estudiante\nOPCION: ")
while(int(opcion)< 1 or int(opcion)> 2):
    opcion = input("ERROR, opción ingresada incorrecta\n1. Quiere agregar un nuevo estudiante\n2. Desea eliminar un estudiante")

if(int(opcion)==1):
    nombre = input("Ingrese el nombre del estudiante que desea agregar: \n").capitalize()
    estudiantes.append(nombre)
else:
    borrar_estudiante = input("\nQue Estudiante desea quitar de la lista?: ")
    if borrar_estudiante in estudiantes:
        print("El estudiante ha sido eliminado!\n")
    else:
        print("No se ha encontrado el estudiante que desea quitar\n")

print("| Lista Actualizada |")
print(f"{estudiantes}")
