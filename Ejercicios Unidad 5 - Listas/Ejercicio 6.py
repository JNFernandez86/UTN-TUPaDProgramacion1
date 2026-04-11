# Ejercicio 6

numeros = [1,88,35,9,71,48,3]
rotar_derecha = []

rotar_derecha.append(numeros[-1])

for n in range(len(numeros)-1):
    rotar_derecha.append(numeros[n])

print(f"La lista rotada a la derecha quedaria: {rotar_derecha}")