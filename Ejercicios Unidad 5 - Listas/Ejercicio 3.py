#Ejercicio 3
import random

numeros = []
pares=[]
impares=[]
#Carga la lista con los 15 elementos aleatorios
for num in range(15):
    numero_entero = random.randint(1,100)
    numeros.append(numero_entero)
#Busca pares e impares y los agrega a la listas de correspondietes
for x in numeros:
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)
#Calcula la cantidad de las listas impar y par
cantidad_impares = len(impares)
cantidad_pares = len(pares)

#Salida
print(f"Se ha registrado {cantidad_impares} números impares\n")
print(f"Se ha registrado {cantidad_pares} números pares\n")
