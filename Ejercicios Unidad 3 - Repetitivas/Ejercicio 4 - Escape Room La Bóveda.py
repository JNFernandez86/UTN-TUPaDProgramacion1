#VARIABLES INICIALES 
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
contador_forzado_cerradura=0

#Ingreso del nombre del agente y su validacion que sea solo texto, sin espacios ni digitos
nombre_agente=input("\nIngrese el nombre del Agente: ")
while nombre_agente=="" or not nombre_agente.isalpha():
    print("Error: Solo se permiten letras. Ni espacios ni números\n")
    nombre_agente=input("Ingrese el nombre del Agente: ")

nombre_agente=nombre_agente.upper() 

# CONDICIÓN DEL BUCLE - Verifica variables hasta que una se correcta exeptuando la alarma
while(energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma):
    print(f"\n<----------STATS---------->\nAGENTE {nombre_agente}: ENERGIA: {energia}, Tiempo: {tiempo} y posee {cerraduras_abiertas} cerraduras Abiertas\n")
    #Ingreso del menu de opciones y eleccion. con validacion, solo permite numeros del 1 al 3
    
    print("################ MENU ################\n")
    print("1) Forzar cerradura \n2) Hackear panel \n3) Descansar\n")
    opcion=input("OPCIÓN: ")
    while opcion=="" or not opcion.isdigit() or not int(opcion) in (1,2,3):
        if opcion=="" or not opcion.isdigit():
            print("ERROR: CARÁCTER NO VÁLIDO -----\n")
        else:
            print("ERROR: OPCIÓN NO VÁLIDA")
        print("################ MENU ################\n")
        print("1) Forzar cerradura \n2) Hackear panel \n3) Descansar\n")
        opcion=input("OPCIÓN: ")
    opcion=int(opcion)
    if(opcion==1):
        #Codigo para la Opcion 1
        print("\n#### FORZAR CERRADURA #####")
        #Inicia contador para que no se pueda ejecutar 3 veces seguidas el Forcejeo. Resta los parametros de energia y tiempo
        contador_forzado_cerradura+=1
        energia -= 20
        tiempo -= 2
        #inicio de condicion con el aviso del activar alarma
        if(energia < 40):
            print("Existe Riesgo de activar alarma")
            numero =""
            #Ingreso y validacion entre numero 1 y 3
            while not numero.isdigit() or (int(numero) != 1 and int(numero) != 2 and int(numero) != 3):
                numero = input("\nIngrese un número del 1 al 3: ")   
            if(int(numero) == 3):
                alarma=True
                break
            else: 
                cerraduras_abiertas+=1
                print("\n Ha abierto una cerradura ")
        elif(contador_forzado_cerradura==3):
            alarma=True
            print("\nATENCIÓN: FORZÓ 3 VECES SEGUIDOAS LA CERRADURA. ")
            print("\nLa cerradura se ha trabado: BOVEDA BLOQUEADA")
            
        else:
            cerraduras_abiertas+=1
            print(f"\nFELICITACIONES: Ha abierto una cerradura quedan {3-cerraduras_abiertas} por encontrar!\n")
        input("\nPresione Enter para continuar")
    #OPCION 2 INTENTO DE HACKEO DE PANEL        
    elif(opcion==2):
        print("\n#### Hackear panel ####\n")
        #Vuelve el contador de forcejeo de cerradura a 0, ya que cambia de opcion. Resta los parametros de energia y tiempo
        contador_forzado_cerradura=0
        energia -= 10
        tiempo -= 3
        #Carga 4 intentos al codigo parcia. si posee una longitud de 8 posiciones, te regala llave, si es que le faltan
        for x in range(4):
            codigo_parcial+="#"
            print(f"Realizando hackeo {x+1}")
        if(len(codigo_parcial)>= 8):
            if(cerraduras_abiertas<3):
                cerraduras_abiertas+=1
                print(f"\nFELICITACIONES: Ha abierto una cerradura!! Quedan {3-cerraduras_abiertas} por encontrar!")
        else:
            print("\nSE HA REALIZADO EL HACKEO SIN ÉXITO")
        input("\nPresione Enter para continuar")        
    else:
        #OPCIÓN 3: Realiza un descanso
        print("\n#### Descanso #####")
        #Vuelve el contador de forcejeo de cerradura a 0, ya que cambia de opcion. suma la energia de 15 puntos y resta el tiempo
        contador_forzado_cerradura=0
        #Verifica que la salud no puede superar 100 puntos.
        if(energia>=85):
            energia=100
        else:
            energia += 15
        tiempo -= 1
        #Alarma activa, se le resta un plus de 10
        if(alarma==True):
            energia-=10
        print(f"\nHA RECUPERADO ENERGÍA ({energia})")

        input("\nPresione Enter para continuar")

#RESULTADO DEL JUEGO
print("\n=== FIN DEL JUEGO ===")
if(alarma==True and tiempo <= 3 or cerraduras_abiertas !=3 ):
    print("\nMISIÓN FALLIDA\n")
elif energia <= 0:
    print("\nMISIÓN FALLIDA: TE QUEDASTE SIN ENERGIA.\n")
elif tiempo<=0:
    print("\nMISIÓN FALLIDA: TE QUEDASTE SIN TIEMPO.\n")
else:
    print("\n¡MISIÓN COMPLETADA! Todas las cerraduras fueron abiertas.\n")
input("Presione Enter para finalizar")