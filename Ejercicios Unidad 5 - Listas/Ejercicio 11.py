# Crear una lista con los nombres de 10 estudiantes.
# ● Solicitar al usuario que ingrese un nombre a buscar.
# ● Indicar si el nombre se encuentra en la lista.
# ● Mostrar la posición en la que aparece.
# ● Si no se encuentra, informar que no está en la lista.

posicion=0
existe_nombre = False
#Creacíon de Lista con los nombres de los estudiantes
estudiantes = ["Fabrillo Canalla","Camila Ortega", "Esteban Praga","Marina Orellena","Marcos Aurelio",
            "Jazmin Fernandez","Pedro Hernandez","Franco Donato","Paola Gutierrez","Marcelo Lima"]
#Solicitud del Nombre del estudiante al usuario
nombre_buscado = input("Ingrese el nombre del estudiante a buscar: ")

#Recorrido de la lista y la busqueda del nombre ingresado
for name in range(len(estudiantes)):
    if estudiantes[name].lower() == nombre_buscado.lower():
        posicion = name
        existe_nombre = True

if existe_nombre == True:
    print(f"\nEl/La Alumno/a {nombre_buscado} se encuentra en la posicion {posicion} de la lista")
else:
    print("\nNo se ha encontrado el nombre del estudiante buscado en la lista")