# Inicializar el tablero de Ta-Te-Ti
tablero = [["-" for f in range(3)] for c in range(3)]
contador = 0
jugador ="X"

while contador < 9:
    
    if(contador%2==0):
        print("Turno Jugador ""X")
        opcion = "X"
    else:
        print("Turno Jugador ""O")
        opcion = "O"
        
    fila = int(input(f"Ingrese el número de fila (1,2 o 3): "))-1
    columna = int(input(f"Ingrese el número de columna (1,2 o 3) : "))-1
    if(fila < 0 or fila > 2 or columna < 0 or columna > 2):
        print("ERROR: Ha ingresado las coordenadas incorrectas\n")
        fila = int(input(f"Ingrese el número de fila (1,2 o 3): "))-1
        columna = int(input(f"Ingrese el número de columna (1,2 o 3) : "))-1
    contador +=1
    while (tablero[fila][columna]=='X' or tablero[fila][columna]=='O'):
        print("\nCOORDENADA OCUPADA: ")
        fila = int(input(f"Ingrese nuevamente el número de fila (1,2 o 3): "))-1
        columna = int(input(f"Ingrese nuevamente número de columna (1,2 o 3) : "))-1
    else:
        tablero[fila][columna] = opcion
    for f in range(len(tablero)):
        print(tablero[f])

print("")
    
    