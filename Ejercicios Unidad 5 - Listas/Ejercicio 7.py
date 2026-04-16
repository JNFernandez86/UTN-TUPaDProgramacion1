# Ejercicio 7

# Acumuladores para sumar las temperaturas mínimas y máximas de la semana
suma_minimas = 0
suma_maximas = 0

# Variables para registrar la mayor amplitud térmica encontrada y el día correspondiente
mayor_amplitud = 0
dia_mayor_amplitud = ""

# Lista de temperaturas semanales: cada sublista contiene [mínima, máxima] del día
temperaturas = [[17,25],[19,31],[13,24],[19,28],[16,22],[22,29],[22,26]]

# Lista de nombres de los días, en el mismo orden que la lista de temperaturas
dias = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]


# Primer recorrido: se acumulan las temperaturas mínimas y máximas de cada día
for dia in temperaturas:
    suma_maximas += int(dia[1])  # Temperatura máxima (índice 1)
    suma_minimas += int(dia[0])  # Temperatura mínima (índice 0)

# Se calcula la cantidad de días y los promedios de temperaturas
cantidad = len(temperaturas)
promedio_max = suma_maximas / cantidad
promedio_minimo = suma_minimas / cantidad

# Segundo recorrido: se calcula la amplitud térmica de cada día
# y se determina cuál fue el día con mayor diferencia entre máxima y mínima
for t in range(len(temperaturas)):
    amplitud_termica = temperaturas[t][1] - temperaturas[t][0]  # Máxima - Mínima
    if amplitud_termica > mayor_amplitud:
        mayor_amplitud = amplitud_termica      # Se actualiza la mayor amplitud encontrada
        dia_mayor_amplitud = dias[t]           # Se guarda el nombre del día correspondiente

# Se muestran los resultados finales
print(f"\nEl promedio de las temperaturas MÁXIMAS es: {promedio_max:.1f}°C")
print(f"El promedio de las temperaturas MÍNIMAS es: {promedio_minimo:.1f}°C")
print(f"El día {dia_mayor_amplitud} fue el que tuvo la mayor amplitud térmica ({mayor_amplitud:.1f}°C)\n")