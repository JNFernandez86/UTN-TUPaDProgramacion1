
#1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

print("<<<<< Frutas y Precios iniciales>>>>>")
print(precios_frutas)

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print("\n<<<<< Frutas y Precios actualizados 1>>>>>")
print(precios_frutas)

#2
print("\n<<<<< Frutas y Precios actualizados 2>>>>>")
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

#3

print("\nLista de frutas")
print("------------------")
lista_frutas=[]

for fruta in precios_frutas:
    lista_frutas.append(fruta)

for fruta in lista_frutas:
    print(f"{fruta}")