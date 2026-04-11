# Listas Ejercicio 1

notas_estudiantes=[]
suma=0
promedio=0.0
i=0
for i in range(10):
    nota=int(input(f"Ingrese la nota del estudiante {i+1}: "))
    while(nota < 0 or nota > 10):
        nota = int(input(f"ERROR, NÚMERO INVÁLIDO. Ingrese la nota(0 al 10) del estudiante {i+1}: "))
    suma += nota
    notas_estudiantes.append(nota)
    
maximo = notas_estudiantes[0]
minimo = notas_estudiantes[0]

for nota in notas_estudiantes:
    if nota > maximo:
        maximo = nota
    if nota < minimo:
        minimo = nota

promedio = float(suma/len(notas_estudiantes)) 
print(f"\nEl promedio de las notas es: {promedio:.2f}")
print(f"La mejor nota es: {maximo}")
print(f"La peor nota es: {minimo}\n")
