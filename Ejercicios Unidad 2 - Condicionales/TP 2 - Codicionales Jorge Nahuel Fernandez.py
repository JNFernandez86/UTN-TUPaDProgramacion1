#Ejercicio 1

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

#Ejercicio 2

nota = int(input("Ingrese la nota final del alumno: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Ejercicio 3

numero = int(input("Ingrese un número: "))

if numero % 2== 0:
    print("Es Par")
else:
    print("Es impar")


#Ejercicio 4

edad = int(input("Ingrese un número: "))

if edad < 12:
    print("Niño/a")
elif (edad >= 12 and edad < 18 ):
    print("Adolescente")
elif (edad >= 18 and edad < 30):
    print("Adulto/a joven")
else:
    print("Adulto/a")

#Ejercicio 5

password = input("Ingrese la contraseña: ")

if len(password) <= 14 and len(password) >=8:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
    
#Ejercicio 6

kWh = int(input("Ingrese el consumo de kWh: "))

if kWh < 150:
    print("Consumo bajo")
elif kWh <= 300 and kWh >= 150:
    print("Consumo medio")
else:
    print("Consumo alto")
    if kWh>= 500:
        print("¡Considere medidas de ahorro energético!")
        
#Ejercicio 7

frase = input("Introduce una frase o palabra: ")
vocales = "aeiouAEIOU"

ultima_letra = frase[-1]

if ultima_letra in vocales:
    print(f"\n{frase}!\n")
else:
    print(f"\n{frase}\n")
 
 
#Ejercicio 8

nombre = input("Ingrese su nombre: ")

print("Elija la opción que desee: ")
print("Opción 1: Su nombre en Mayúsculas")
print("Opción 2: Su nombre en Minúsculas")
print("Opción 3: Su nombre en con la primer letra en mayúscula")
opcion = int(input("Ingrese la opción elegida: "))

if opcion == 1:
    print(f"{nombre.upper()}")
elif opcion == 2:
    print(f"{nombre.lower()}")
else:
     print(f"{nombre.title()}")
 
 #Ejercicio 9

magnitud = float(input("Ingrese la magnitud del terremoto en escala Ritcher: "))

texto = "Categroia del terremoto: "

if magnitud < 3:
    print("\n" + texto + "Muy Leve (imperceptible)\n")
elif magnitud >= 3 and magnitud < 4:
    print("\n" +texto + "Leve (ligeramente perceptible).\n")
elif magnitud >= 4 and magnitud < 5:
    print("\n" +texto + "Moderado (sentido por personas, pero generalmente no causa daños).\n")
elif magnitud >= 5 and magnitud < 6:
    print("\n" +texto + "Fuerte (puede causar daños en estructuras débiles).\n")
elif magnitud >= 6 and magnitud < 7:
    print("\n" +texto + "Muy fuerte (puede causar daños significativos).\n")
else:
    print(texto + "\nExtremo (puede causar graves daños a gran escala).\n")


#Ejercicio 10

hemisferio = input("Ingrese el hemisferio N(norte) o S(sur): ").upper()
mes = int(input("Ingrese el mes en número: (1 al 12) "))
dia = int(input("Ingrese el número de dia: "))

texto = "La Estación del año es: "
       
if hemisferio == "S":
    if(mes <= 1 or mes <= 12):
        if(mes==2 and (dia < 1 or dia < 28 )):
            if (mes == 12 and dia >=21) or (mes == 3 and dia <=20) or mes == 1 or mes == 2:
                print("\n"+ texto + "ES VERANO\n")
            elif (mes == 12 and dia < 21) or (mes== 9 and dia >=21) or mes == 10 or mes == 11:
                print("\n"+ texto + "ES PRIMAVERA\n")
            elif (mes == 6 and dia < 21) or (mes== 3 and dia >=21) or mes == 4 or mes == 5:
                print("\n"+ texto + "ES OTOÑO\n")
            else:
                print("\n"+ texto + "ES INVIERNO\n")

        elif((mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12) and (dia < 1 or dia < 31 )):
            if (mes == 12 and dia >=21) or (mes == 3 and dia <=20) or mes == 1 or mes == 2:
                    print("\n"+ texto + "ES VERANO\n")
            elif (mes == 12 and dia < 21) or (mes== 9 and dia >=21) or mes == 10 or mes == 11:
                    print("\n"+ texto + "ES PRIMAVERA\n")
            elif (mes == 6 and dia < 21) or (mes== 3 and dia >=21) or mes == 4 or mes == 5:
                    print("\n"+ texto + "ES OTOÑO\n")
            else:
                    print("\n"+ texto + "ES INVIERNO\n")

        elif(mes==4 or mes==6 or mes==9 or mes==11 and (dia < 1 or dia < 30 )):
            if (mes == 12 and dia >=21) or (mes == 3 and dia <=20) or mes == 1 or mes == 2:
                    print("\n"+ texto + "ES VERANO\n")
            elif (mes == 12 and dia < 21) or (mes== 9 and dia >=21) or mes == 10 or mes == 11:
                print("\n"+ texto + "ES PRIMAVERA\n")
            elif (mes == 6 and dia < 21) or (mes== 3 and dia >=21) or mes == 4 or mes == 5:
                print("\n"+ texto + "ES OTOÑO\n")
            else:
                print("\n"+ texto + "ES INVIERNO\n")
        else:
            print("Ha ingresado un numero de día INCORRECTO!! con respecto al mes o un numero mayor a 31.")
    else:
        print("Ha ingresado un numero correspondiente al mes INCORRECTO!!")

  
elif hemisferio == "N":
        if(mes <= 1 or mes <= 12):
            if(mes==2 and (dia < 1 or dia < 28 )):
                if (mes == 12 and dia >=21) or (mes == 3 and dia <=20) or mes == 1 or mes == 2:
                    print("\n"+ texto + "ES INVIERNO\n")
                elif (mes == 12 and dia < 21) or (mes== 9 and dia >=21) or mes == 10 or mes == 11:
                    print("\n"+ texto + "ES OTOÑO\n")
                elif (mes == 6 and dia < 21) or (mes== 3 and dia >=21) or mes == 4 or mes == 5:
                    print("\n"+ texto + "ES PRIMAVERA\n")
                else:
                    print("\n"+ texto + "ES VERANO\n")

            elif((mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12) and (dia < 1 or dia < 31 )):
                if (mes == 12 and dia >=21) or (mes == 3 and dia <=20) or mes == 1 or mes == 2:
                    print("\n"+ texto + "ES INVIERNO\n")
                elif (mes == 12 and dia < 21) or (mes== 9 and dia >=21) or mes == 10 or mes == 11:
                    print("\n"+ texto + "ES OTOÑO\n")
                elif (mes == 6 and dia < 21) or (mes== 3 and dia >=21) or mes == 4 or mes == 5:
                    print("\n"+ texto + "ES PRIMAVERA\n")
                else:
                    print("\n"+ texto + "ES VERANO\n")
            elif(mes==4 or mes==6 or mes==9 or mes==11 and (dia < 1 or dia < 30 )):
                if (mes == 12 and dia >=21) or (mes == 3 and dia <=20) or mes == 1 or mes == 2:
                    print("\n"+ texto + "ES INVIERNO\n")
                elif (mes == 12 and dia < 21) or (mes== 9 and dia >=21) or mes == 10 or mes == 11:
                    print("\n"+ texto + "ES OTOÑO\n")
                elif (mes == 6 and dia < 21) or (mes== 3 and dia >=21) or mes == 4 or mes == 5:
                    print("\n"+ texto + "ES PRIMAVERA\n")
                else:
                    print("\n"+ texto + "ES VERANO\n")
            else:
                print("Ha ingresado un numero de día INCORRECTO!! con respecto al mes o un numero mayor a 31.")
        else:
            print("Ha ingresado un numero correspondiente al mes INCORRECTO!!")
else:
    print("ha ingresado una opción incorrecta en el hemisferio")

print("Saliendo del programa...\n")
 
 