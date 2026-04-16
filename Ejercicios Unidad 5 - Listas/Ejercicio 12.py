# Ejercicio 12

# Creación de la lista con 8 posiciones inicializadas en 0
numeros = [0 for n in range(8)]

# Carga de la lista: se solicita un número entero por cada posición
for n in range(len(numeros)):
    number = input("Ingrese un número entero: ")

    # Validación: se repite el ingreso mientras el valor no sea un número entero
    # .isdigit() devuelve True solo si todos los caracteres son dígitos numéricos
    while number.isdigit() == False:
        print("ERROR: No ha ingresado un número entero\n")
        number = input("Ingrese un número entero: ")

    # Se almacena el valor validado en la posición actual de la lista
    numeros[n] = number

# Se muestra la lista tal como fue ingresada por el usuario
print("\n<<<<< Lista ORIGINAL >>>>>\n")
print(numeros)

# sorted() devuelve una nueva lista ordenada de menor a mayor sin modificar la original
ordenada_ascendente = sorted(numeros)

print("\n<<<<< Lista ordenada de menor a mayor >>>>>\n")
print(ordenada_ascendente)

# .reverse() invierte la lista en el lugar, convirtiéndola de mayor a menor
print("\n<<<<< Lista ordenada de mayor a menor >>>>>\n")
ordenada_ascendente.reverse()
print(ordenada_ascendente)

print("")