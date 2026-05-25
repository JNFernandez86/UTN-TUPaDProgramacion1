# Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

paises_original = {"Argentina":"Buenos Aires","Brasil":"Brasilia","Chile":"Santiago", 
                "Peru":"Lima","Paraguay":"Asunción","Uruguay":"Montevideo"}

provincias_paises = dict()

for valor, clave in paises_original.items():
    provincias_paises[clave] = valor

print("Lista Original")
print(paises_original)
print("\nLista cambiada clave por valor")
print(provincias_paises)