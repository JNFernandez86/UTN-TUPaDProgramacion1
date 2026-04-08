#Ejercicio 1 #

print("Hola Mundo!")


#Ejercicio 2 #

nombre = input("Ingrese un nombre:")

print(f"Bienvenido {nombre} !")

# Ejercico 3 

nombre = input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
lugar_residencia= input("Ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}")

# Ejercico 4 #

import math

radio = float(input(("Ingrese en cm el radio a calcular: ")))
area = float(radio * math.pi)**2
perimetro = float(2 *math.pi * radio)

print(f"El perimetro es {perimetro:.2f} cm y el área es {area:.2f} cm2 ")  

#Ejercicio 5

horas = 0

segundos = int(input("Ingrese la cantidad de segundos para calcular: "))

horas = int(segundos / 3600)

print(f"{segundos} segundos, equivalen a {horas} horas")

# Ejercico 6 #


numero = int(input("Ingrese un numero: "))
total = 0


total = int(numero * 1)
print(f"{numero} X  1 = {total}")
total = int(numero * 2)
print(f"{numero} X  2 = {total}")
total = int(numero * 3)
print(f"{numero} X  3 = {total}")
total = int(numero * 4)
print(f"{numero} X  4 = {total}")
total = int(numero * 5)
print(f"{numero} X  5 = {total}")
total = int(numero * 6)
print(f"{numero} X  6 = {total}")
total = int(numero * 7)
print(f"{numero} X  7 = {total}")
total = int(numero * 8)
print(f"{numero} X  8 = {total}")
total = int(numero * 9)
print(f"{numero} X  9 = {total}")
total = int(numero * 10)
print(f"{numero} X 10 = {total}")


    
#Ejercicio 7 #

numero1 = int(input("Ingrese un número entero: "))
numero2 = int(input("Ingrese otro número entero DISTINTO a 0: "))

sumar = numero1 + numero2
restar = numero1-numero2
multiplicacion = numero1*numero2
division = float(numero1/numero2)

print(f"La sumar es: {sumar}")
print(f"La restar es: {restar}")
print(f"La multiplicación es: {multiplicacion}")
print(f"La división es: {division:.2f}")

#Ejercicio 8

altura=0
peso = 0
imc = 0

altura = float(input("Ingrese su altura en metros, Ej 1.85:   "))
peso = int(input("Ingrese el peso en kilos: "))
imc = float(peso) / (altura ** 2)

print(f"Su índice de masa corporal es: {imc}")



#Ejercicio 9

celsius = float(input("Ingrese la temperatura a convertir (°C): "))

fahrenheit = float((9/5)* celsius + 32)

print(f"{celsius}°C, equivalen a {fahrenheit}°F")


#Ejercicio 10 #


numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

promedio = float((numero1 + numero2 + numero3)/3)

print(f"El promedio es: {promedio:.2f}")
