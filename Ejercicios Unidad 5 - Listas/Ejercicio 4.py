# Ejercicio 4

datos = [1,3,5,3,7,1,9,5,3]

sin_repetidos = []

#Busqueda si existe algún número repetido y lo agrega a la lista vacia
for item in datos:
    if item not in sin_repetidos:
        sin_repetidos.append(item)

print(f" Lista sin repetidos\n")

#Muestra la lista sin repetidos
for dato in sin_repetidos:
    print(f"{dato}\n")

