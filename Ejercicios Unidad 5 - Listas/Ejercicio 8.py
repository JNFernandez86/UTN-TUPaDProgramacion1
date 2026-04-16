# Ejercicio 8

# Matriz de notas: cada fila es un estudiante, cada columna es una materia
estudiantes = [
    [ 7, 9, 6],  # Estudiante 1
    [ 8, 8, 4],  # Estudiante 2
    [10, 7, 9],  # Estudiante 3
    [ 4, 8, 9],  # Estudiante 4
    [ 2, 4, 8]]  # Estudiante 5

# Variable para almacenar el promedio de cada estudiante (se reutiliza en cada iteración)
promedio_estudiante = 0

# Cantidad de filas de la matriz (un valor por cada estudiante)
cantidad_estudiantes = len(estudiantes)

# ---- SECCIÓN 1: Promedio por alumno ----
# Se recorre cada fila de la matriz para calcular el promedio de sus notas
print("\n<----- PROMEDIOS POR ALUMNO ----->")
for i in range(cantidad_estudiantes):
    # Se obtienen las notas del estudiante actual (fila i)
    notas = estudiantes[i]
    # Acumulador para sumar las notas del estudiante actual
    suma_estudiante = 0
    # Se suman todas las notas del estudiante
    for nota in notas:
        suma_estudiante += nota
    # Se calcula el promedio dividiendo la suma por la cantidad de materias
    promedio_estudiante = suma_estudiante / len(notas)
    print(f"El promedio alumno {i+1}: {promedio_estudiante:.2f}")

# ---- SECCIÓN 2: Promedio por materia ----
# Se recorre cada columna de la matriz para calcular el promedio de cada materia
print("\n<----- PROMEDIOS POR MATERIA ----->")
for materia in range(3):
    # Acumulador para sumar las notas de todos los estudiantes en esta materia
    suma_materia = 0
    # Se recorre cada estudiante (fila) y se acumula su nota en la materia actual
    for estudiante in range(cantidad_estudiantes):
        suma_materia += estudiantes[estudiante][materia]
    # Se calcula el promedio dividiendo la suma por la cantidad de estudiantes
    promedio_materia = suma_materia / cantidad_estudiantes 
    print(f"El Promedio materia {materia+1} es de: {promedio_materia:.2f}")
print("\n")