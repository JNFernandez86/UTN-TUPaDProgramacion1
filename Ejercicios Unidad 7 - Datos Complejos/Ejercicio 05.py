# 5)

mensaje = input("Ingrese la frase que desea: ")

palabras = mensaje.split()
palabras_unicas = set(palabras)
conteo_palabras = {}

for palabra in palabras:
    conteo_palabras[palabra] = conteo_palabras.get(palabra, 0) + 1

print("Palabras únicas:", palabras_unicas)
print("Conteo de palabras:", conteo_palabras)