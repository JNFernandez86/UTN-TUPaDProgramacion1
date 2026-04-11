# Ejercicio 12

#Creación e inicialización de la lista Numeros
numeros = [0 for n in range(8)]

#Carga de la lista
for n in range(len(numeros)):
    number = input("Ingrese un número entero: ")
    while number.isdigit() == False:
        print("ERROR: No ha ingreado un numero entero\n")
        number = input("Ingrese un número entero: ")
    numeros[n] = number

#Mostrar lista cargada
print("\n<<<<< Lista ORIGINAL >>>>>\n")
print(numeros)
ordenada_ascendente = sorted(numeros)

#Lista ordenada de Mayor a menor mediante la función Sorted
print("\n<<<<< Lista ordenada de menor a mayor >>>>>\n")

print(ordenada_ascendente)
print("\n<<<<< Lista ordenada de mayor a menor >>>>>\n")

ordenada_ascendente.reverse()
print(ordenada_ascendente)
print("")