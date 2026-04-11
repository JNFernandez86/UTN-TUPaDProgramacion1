# Ejercicio 6

# Inicialización de la lista original con los números a rotar
numeros = [1, 88, 35, 9, 71, 48, 3]

# Inicialización de la lista que almacenará el resultado de la rotación
rotar_derecha = []

# Se agrega primero el último elemento de la lista original,
# ya que en una rotación a la derecha este pasa a ser el primero
rotar_derecha.append(numeros[-1])

# Se recorre la lista original desde el primer elemento hasta el anteúltimo
# (excluyendo el último, que ya fue agregado al inicio)
for n in range(len(numeros) - 1):
    rotar_derecha.append(numeros[n])

# Se imprime la lista rotada a la derecha
print(f"La lista rotada a la derecha queda: {rotar_derecha}")