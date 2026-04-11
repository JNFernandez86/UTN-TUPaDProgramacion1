# Ejercicio 11

# Posición donde se encontrará el nombre buscado (se actualiza si existe)
posicion = 0

# Bandera que indica si el nombre fue encontrado en la lista
existe_nombre = False

# Lista con los nombres de los estudiantes
estudiantes = ["Fabrillo Canalla", "Camila Ortega", "Esteban Praga", "Marina Orellena", "Marcos Aurelio",
            "Jazmin Fernandez", "Pedro Hernandez", "Franco Donato", "Paola Gutierrez", "Marcelo Lima"]

# Se solicita al usuario el nombre a buscar
nombre_buscado = input("Ingrese el nombre del estudiante a buscar: ")

# Se recorre la lista comparando cada nombre con el buscado
# .lower() en ambos lados permite una búsqueda sin distinguir mayúsculas/minúsculas
for name in range(len(estudiantes)):
    if estudiantes[name].lower() == nombre_buscado.lower():
        posicion = name        # Se guarda el índice donde fue encontrado
        existe_nombre = True   # Se activa la bandera de encontrado

# Se muestra el resultado según si el nombre fue encontrado o no
if existe_nombre:
    print(f"\nEl/La Alumno/a {nombre_buscado} se encuentra en la posición {posicion} de la lista")
else:
    print("\nNo se ha encontrado el nombre del estudiante buscado en la lista")