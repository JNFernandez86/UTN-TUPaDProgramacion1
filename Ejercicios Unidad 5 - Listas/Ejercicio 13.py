# Ejercicio 13

puntajes = [450, 1200, 875, 990, 300, 1500, 640]

cantidad_puntaje = len(puntajes)

#Inicialización de los índices para la busqueda del puntaje 990
inicio = 0
puntaje_buscado = -1
final=len(puntajes) - 1

#Se busca el valor de forma binaria
while (inicio <= final) and (puntaje_buscado==-1):
    
    #Se busca la mitad de la lista
    medio = (inicio + final)//2
    
    if puntajes[medio] == 990: #Si el valor buscado es encontrado en el medio de la lista, guarda la ubicación del indice
        puntaje_buscado = medio
    else:
        if puntajes[medio] < 990:#El indíce se detecta del lado derecho
            inicio = medio + 1
        else: #El índice se encuentra del lado izquierdo
            final = medio - 1

# #Algoritmo de busqueda por método de burbuja.
for elementos in range(cantidad_puntaje -1):
    for recorrido in range(cantidad_puntaje - 1 - elementos):
        if puntajes[recorrido] < puntajes[recorrido+1]:
            puntajes[recorrido], puntajes[recorrido + 1] = puntajes[recorrido + 1], puntajes[recorrido]

#SALIDAS DE CONSOLA
print(f"\nEl puntaje mas ALTO es: {puntajes[0]} \n")
print(f"El puntaje mas BAJO es: {puntajes[cantidad_puntaje-1]} \n")
print("<----- PUNTAJES -----> ")

#Listar cada uno de los puntajes para que aparezcan uno abajo del otro mostrando el Ranking
for x in range(cantidad_puntaje):
    print(f"RANKING #{x+1}: {puntajes[x]}")
print("<-------------------> \n")

if puntaje_buscado == -1:
    print("El puntaje 990 no se ha encontrado")
else:
    print(f"El puntaje 990 ha sido encontrado en la posicion {puntaje_buscado}\n")
