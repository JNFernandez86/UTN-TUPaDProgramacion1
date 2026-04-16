#Ejercicio 9

# Inicializar el tablero de Ta-Te-Ti como una matriz 3x3 rellena con "-"
tablero = [["-" for f in range(3)] for c in range(3)]

# Contador de turnos jugados (máximo 9 en un tablero 3x3)
contador = 0

# Bucle principal del juego: se repite hasta que se completen los 9 turnos o haya un ganador
while contador < 9:

    # Se determina el turno según si el contador es par (X) o impar (O)
    if contador % 2 == 0:
        print("\nTurno Jugador X\n")
        opcion = "X"
    else:
        print("\nTurno Jugador O\n")
        opcion = "O"

    # Se solicitan las coordenadas al jugador (se resta 1 para convertir a índice 0-based)
    fila = int(input("Ingrese el número de fila (1, 2 o 3): ")) - 1
    columna = int(input("Ingrese el número de columna (1, 2 o 3): ")) - 1

    # Validación de rango: si las coordenadas están fuera del tablero, se vuelven a pedir
    if fila < 0 or fila > 2 or columna < 0 or columna > 2:
        print("ERROR: Ha ingresado las coordenadas incorrectas\n")
        fila = int(input("Ingrese el número de fila (1, 2 o 3): ")) - 1
        columna = int(input("Ingrese el número de columna (1, 2 o 3): ")) - 1

    # Validación de celda ocupada: si la celda ya tiene una ficha, se repiten las coordenadas
    while tablero[fila][columna] == "X" or tablero[fila][columna] == "O":
        print("\nCOORDENADA OCUPADA: ")
        fila = int(input("Ingrese nuevamente el número de fila (1, 2 o 3): ")) - 1
        columna = int(input("Ingrese nuevamente el número de columna (1, 2 o 3): ")) - 1

    # Se coloca la ficha del jugador en la celda validada
    tablero[fila][columna] = opcion

    # Se cuenta el turno recién jugado (ahora después de confirmar la jugada)
    contador += 1

    # Se imprime el estado actual del tablero después de cada turno
    for f in range(len(tablero)):
        print(tablero[f])
    
    