# 6)

alumno = {}

for i in range(3):
    nombre =  input("\nIngrese el nombre del alumno: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} del alumno {nombre}: "))
        notas.append(nota)
    alumno[nombre] = tuple(notas)

print("\nPromedio de cada alumno:")
for nombre, notas in alumno.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es: {promedio:.2f}")
    
