# Ejercicio 7

suma_minimas =0
suma_maximas = 0
mayor_amplitud=0
dia_mayor_amplitud = ""

temperaturas =[[17,25],[19,31],[13,24],[19,28],[16,22],[22,29],[22,26]]
dias = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]


for dia in temperaturas:
    suma_maximas += int(dia[1])
    suma_minimas += int(dia[0])
    
cantidad = len(temperaturas)
promedio_max = suma_maximas / cantidad
promedio_minimo = suma_minimas / cantidad

for t in range(len(temperaturas)):
    amplitud_termica  = temperaturas[t][1] - temperaturas[t][0]
    if(amplitud_termica > mayor_amplitud):
        mayor_amplitud = amplitud_termica
        dia_mayor_amplitud = dias[t]
        
print(f"El promedio de las temparaturas MÁXIMAS es: {promedio_max:.1f}°C")
print(f"El promedio de las temparaturas MÍNIMAS es: {promedio_minimo:.1f}°C")
print(f"El día {dia_mayor_amplitud} fue el que tuvo la mayor amplitud térmica ({mayor_amplitud:.1f}°C)")