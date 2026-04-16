# Ejercicio 13

# Lista de puntajes a analizar
puntajes = [450, 1200, 875, 990, 300, 1500, 640]

# Cantidad total de puntajes en la lista
cantidad_puntaje = len(puntajes)


# ---- SECCIÓN 1: Búsqueda binaria del puntaje 990 ----

# Índices de inicio y fin que delimitan el rango de búsqueda
inicio = 0
final = len(puntajes) - 1

# Variable que almacenará el índice donde se encontró el puntaje (-1 si no se encuentra)
puntaje_buscado = -1

# Se repite mientras el rango sea válido y no se haya encontrado el valor
while (inicio <= final) and (puntaje_buscado == -1):

    # Se calcula el índice del elemento central del rango actual
    medio = (inicio + final) // 2

    if puntajes[medio] == 990:
        # El valor buscado está en el centro: se guarda su índice
        puntaje_buscado = medio
    elif puntajes[medio] < 990:
        # El valor buscado es mayor: se descarta la mitad izquierda
        inicio = medio + 1
    else:
        # El valor buscado es menor: se descarta la mitad derecha
        final = medio - 1


# ---- SECCIÓN 2: Ordenamiento por método de burbuja (de mayor a menor) ----
# Compara pares adyacentes y mueve el mayor hacia la izquierda en cada pasada.
# Se necesitan (n-1) pasadas para garantizar que la lista quede completamente ordenada.
for elementos in range(cantidad_puntaje - 1):

    # En cada pasada, los últimos 'elementos' ya están en su posición correcta
    for recorrido in range(cantidad_puntaje - 1 - elementos):

        # Si el elemento actual es menor que el siguiente, se intercambian
        if puntajes[recorrido] < puntajes[recorrido + 1]:
            puntajes[recorrido], puntajes[recorrido + 1] = puntajes[recorrido + 1], puntajes[recorrido]


# ---- SECCIÓN 3: Salidas por consola ----

# Tras el ordenamiento descendente, el mayor queda en el índice 0 y el menor en el último
print(f"\nEl puntaje más ALTO es: {puntajes[0]}\n")
print(f"El puntaje más BAJO es: {puntajes[cantidad_puntaje - 1]}\n")

# Se listan los puntajes ordenados mostrando el ranking de cada posición
print("<----- PUNTAJES ----->")
for x in range(cantidad_puntaje):
    print(f"RANKING #{x + 1}: {puntajes[x]}")
print("<------------------->\n")

# Se informa si el puntaje 990 fue encontrado y en qué posición
if puntaje_buscado == -1:
    print("El puntaje 990 no se ha encontrado")
else:
    print(f"El puntaje 990 ha sido encontrado en la posición {puntaje_buscado}\n")