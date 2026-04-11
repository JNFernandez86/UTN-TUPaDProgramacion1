# Listas Ejercicio 1

notas_estudiantes=[]
suma=0
promedio=0.0
i=0
#Ingreso de las notas y guardadas en la lista
for i in range(10):
    nota=input(f"Ingrese la nota del estudiante {i+1}: ")
    #Manejo de exepciones, que permita solo números y las notas esten entre 0 y 10
    while(nota.isdigit() == False or int(nota) < 0 or int(nota) > 10):
        nota = input(f"ERROR, NÚMERO INVÁLIDO . Ingrese la nota(0 al 10) del estudiante {i+1}: ")
    suma += int(nota) #Acumula la suma de las notas para luego sacar el promedio
    notas_estudiantes.append(nota)

#Inicialización de Máximos y mínimos   
maximo = notas_estudiantes[0]
minimo = notas_estudiantes[0]

#Recorrido de la lista, buscando máximos y mínimos
for nota in notas_estudiantes:
    if nota > maximo:
        maximo = nota
    if nota < minimo:
        minimo = nota
#Cálculo del promedio
promedio = float(suma/len(notas_estudiantes)) 

#SALIDAS
print(f"\nEl promedio de las notas es: {promedio:.2f}")
print(f"La mejor nota es: {maximo}")
print(f"La peor nota es: {minimo}\n")
