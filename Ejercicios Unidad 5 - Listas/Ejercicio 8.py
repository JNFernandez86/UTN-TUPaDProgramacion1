# Ejercicio 8

estudiantes = [[7,9,6],[8,8,4],[10,7,9],[4,8,9],[2,4,8]]
suma_materia=0
promedio_estudiante=0

# for i in range(len(estudiantes)):
#     fila = estudiantes[i]
#     promedio = sum(fila) / len(fila)
#     print(f"Estudiante {i+1}: promedio = {promedio:.2f}")

for i in range(len(estudiantes)):
    notas = estudiantes[i]
    suma_materia=0
    for nota in notas:
        suma_materia += nota
    promedio_estudiante = suma_materia / len(notas)
    
    
    print(f"El promedio del estudiante {i+1} es: {promedio_estudiante:.2f}  ")
