#Ejercicio 3
import random

numeros = []
pares=[]
impares=[]

for num in range(15):
    numero_entero = random.randint(1,100)
    numeros.append(numero_entero)

for x in numeros:
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)

cantidad_impares = len(impares)
cantidad_pares = len(pares)

print(f"Se ha registrado {cantidad_impares} números impares\n")
print(f"Se ha registrado {cantidad_pares} números pares\n")
