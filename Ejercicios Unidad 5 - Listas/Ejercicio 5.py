# Ejercicio 5

#Carga de la lista Estudiantes
estudiantes = ['Marcos','Pedro','Laura','Lucas','Jorge','Milagros','Nahuel','Abel']

#Menú de opciones 
opcion = input("\n_MENU_\n1. Quiere agregar un nuevo estudiante\n2. Desea eliminar un estudiante\nOPCION: ")
#Manejo de excepciones para que solo sea permitido 1 o 2
while(opcion.isdigit() == False or int(opcion)< 1 or int(opcion)> 2 ):
    opcion = input("\nERROR, opción ingresada incorrecta. Opción 1 o 2.\n\n1. Quiere agregar un nuevo estudiante\n2. Desea eliminar un estudiante\nOPCION:")

#Opcion 1 Agregar Estudiante
if(int(opcion)==1):
    nombre = input("Ingrese el nombre del estudiante que desea agregar: ").capitalize()
    estudiantes.append(nombre)
#Opcion 2 Eliminar
else:
    borrar_estudiante = input("\nQue Estudiante desea quitar de la lista?: ").capitalize()
    #Validación para el nombre del estudiante sin espacios ni números                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    while borrar_estudiante.isalpha == False:
        print("ERROR, No se permiten números ni espacios")
    
    if borrar_estudiante in estudiantes:
        print("El estudiante ha sido eliminado!\n")
    else:
        print("No se ha encontrado el estudiante que desea quitar\n")
#Mostrar lista Actualizada, con o sin los cambios
print("| Lista Actualizada |")
print(f"{estudiantes}")
