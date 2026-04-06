# INICALIZACION DE VARIABLES
turno_lunes1=""
turno_lunes2=""
turno_lunes3=""
turno_lunes4=""
turno_martes1=""
turno_martes2=""
turno_martes3=""
dias_libres_lunes=0
dias_ocupados_lunes=0
dias_libres_martes=0
ddias_ocupados_martes=0

print("\n<------    AGENDA TURNOS     ------->\n")

#Solicitud de Nombre del operador
nombre_operador = input("Ingrese nombre del OPERADOR: ")
while(nombre_operador.isalpha()==False): #Validacion de nombre ingresado (Solo letras, sin espacios y sin números)
    nombre_operador= input("ERROR: no se permite vacio y se permiten solo letras.\nIngrese nuevamente el nombre del OPERADOR: ")

print("\n<----- MENU DE OPCIONES ------>\n")
print("1) Reservar turno\n2) Cancelar turno (por nombre)\n3) Ver agenda del día\n4) Ver resumen general\n5) Cerrar sistema\n<---------------------------->\n")
opcion= input("¿Que desea realizar? OPCIÓN: ")

while(opcion!='5'): #Si ingresa 5 sale del programa.
    while(opcion.isdigit()==False):
        opcion= input("\nERROR: INGRESE UN NÚMERO VÁLIDO: ")
    match int(opcion):
        # Opcion 1: Reserva de turno
            case 1:
                print("\nReserva de turnos")
                dia_elegido = ""
                while not dia_elegido.isdigit() or (int(dia_elegido) != 1 and int(dia_elegido) != 2): #Validacion de opciones 1 y 2. Además de que sea un número
                    dia_elegido = input("\nSeleccione el día para reservar (1=Lunes, 2=Martes): ")

                    if not dia_elegido.isdigit():
                        print("\nERROR: Ingrese solo números.")
                    elif int(dia_elegido) not in (1, 2):
                        print("\nERROR: Opción inválida. Use 1 o 2.")

                dia_elegido = int(dia_elegido)
                nombre_paciente= input("Ingrese el nombre del paciente: ")
                while(nombre_paciente.isalpha()==False):#Validacion de nombre paciente ingresado (Solo letras, sin espacios y sin números)
                    nombre_paciente= input("\nERROR: ingresar sólo letras!.\nIngrese el nombre del paciente: ")
                #Eleccion de dia 1-Lunes 2-Martes
                if int(dia_elegido) == 1:
                    if(turno_lunes1.lower() == nombre_paciente.lower() or turno_lunes2.lower() == nombre_paciente.lower() or
                        turno_lunes3.lower() == nombre_paciente.lower() or turno_lunes4.lower() == nombre_paciente.lower()):
                        print(f"Ya existe un turno para el paciente {nombre_paciente}") # Compara si el nombre del paciente esta ingreado en algun turno del lunes
                    #Sino existe el paciente, lo agrega al primer turno disponible
                    elif(turno_lunes1==""):
                        turno_lunes1 = nombre_paciente
                        print(f"\nEl turno ha sido asignado correctamente para {nombre_paciente}")
                    elif(turno_lunes2==""):
                        turno_lunes2 = nombre_paciente
                        print(f"\nEl turno ha sido asignado correctamente para {nombre_paciente}")
                    elif(turno_lunes3==""):
                        turno_lunes3 = nombre_paciente
                        print(f"\nEl turno ha sido asignado correctamente para {nombre_paciente}")
                    elif(turno_lunes4==""):
                        turno_lunes4 = nombre_paciente
                        print(f"\nEl turno ha sido asignado correctamente para {nombre_paciente}")
                    else:
                        print("Todos los turnos del lunes se encuentran ocupados")
                        
                elif int(dia_elegido) == 2:
                    if(turno_martes1.lower() == nombre_paciente.lower() or turno_martes2.lower() == nombre_paciente.lower() or
                        turno_martes3.lower() == nombre_paciente.lower()):
                        print(f"\nYa existe un turno para el paciente {nombre_paciente}") #Compara si el nombre del paciente esta ingreado en algun turno del Martes
                    #Sino existe el paciente, lo agrega al primer turno disponible
                    elif(turno_martes1==""):
                        turno_martes1 = nombre_paciente
                        print(f"\nEl turno ha sido asignado correctamente para {nombre_paciente}")
                    elif(turno_martes2==""):
                        turno_martes2 = nombre_paciente
                        print(f"\nEl turno ha sido asignado correctamente para {nombre_paciente}")
                    elif(turno_martes3==""):
                        turno_lunes3 = nombre_paciente
                        print(f"\nEl turno ha sido asignado correctamente para {nombre_paciente}")
                    else:
                        print("Todos los turnos del martes se encuentran ocupados")
                input("\nPresione Enter para continuar... ")
            # Opción 2 - Cancelar Turnos
            case 2:
                print("\nCancelación de turnos\n")
                dia_cancelar = ""
                while not dia_cancelar.isdigit() or (int(dia_cancelar) != 1 and int(dia_cancelar) != 2): #Validacion de opciones 1 y 2. Además de que sea un número
                    dia_cancelar = input("\nSeleccione el día para reservar (1=Lunes, 2=Martes): ")
                    if not dia_cancelar.isdigit():
                        print("\nERROR: Ingrese solo números.")
                    elif int(dia_cancelar) not in (1, 2):
                        print("\nERROR: Opción inválida. Use 1 o 2.")

                dia_cancelar = int(dia_cancelar)
                nombre_cancelar= input("Ingrese el nombre del paciente: ")
                while(nombre_cancelar.isalpha()==False):
                    nombre_cancelar= input("ERROR: ingresar sólo letras!.\nIngrese el nombre del paciente")
                if(int(dia_cancelar) == 1):
                #Compara si el nombre del paciente esta ingreado en algun turno del Lunes. Si lo esta lo borra en el turno que lo encuentra
                    if(turno_lunes1.lower() == nombre_cancelar.lower()):
                        turno_lunes1 =""
                        print("\nTurno 1 del Lunes cancelado.")
                    elif(turno_lunes2.lower() == nombre_cancelar.lower()):
                        turno_lunes2 =""
                        print("\nTurno 2 del Lunes cancelado.")
                    elif(turno_lunes3.lower() == nombre_cancelar.lower()):
                        turno_lunes3 =""
                        print("\nTurno 3 del Lunes cancelado.")
                    elif(turno_lunes4.lower() == nombre_cancelar.lower()):
                        turno_lunes4 =""
                        print("\nTurno 4 del Lunes cancelado.")
                    else:
                        print(f"No se encontró a '{nombre_cancelar}' en los turnos del Lunes.")
                if(int(dia_cancelar) == 2):
                #Compara si el nombre del paciente esta ingreado en algun turno del Martes. Si lo esta lo borra en el turno que lo encuentra
                    if(turno_lunes1.lower() == nombre_cancelar.lower()):
                        turno_lunes1 =""
                        print("\nTurno 1 del Martes cancelado.")
                    elif(turno_lunes2.lower() == nombre_cancelar.lower()):
                        turno_lunes2 =""
                        print("\nTurno 2 del Martes cancelado.")
                    elif(turno_lunes3.lower() == nombre_cancelar.lower()):
                        turno_lunes3 =""
                        print("\nTurno 3 del Martes cancelado.")
                    else:
                        print(f"No se encontró a '{nombre_cancelar}' en los turnos del Martes.")
                input("\nPresione Enter para continuar... ")
            #OPCIÓN 3 - Resumen de turnos
            case 3:
                print("\nRESUMEN DE TURNOS\n")
                #Pasa por todas las variables buscando el nombre del paciente que tiene turno y los que quedan libres
                if(turno_lunes1==""):
                    print(f"Día Lunes,  TURNO 1: LIBRE")
                else:
                    print(f"Día Lunes,  TURNO 1: {turno_lunes1}")
                if(turno_lunes2==""):
                    print(f"Día Lunes,  TURNO 2: LIBRE")
                else:
                    print(f"Día Lunes,  TURNO 2: {turno_lunes2}")
                if(turno_lunes3==""):
                    print(f"Día Lunes,  TURNO 3: LIBRE")
                else:
                    print(f"Día Lunes,  TURNO 3: {turno_lunes3}")
                if(turno_lunes4==""):
                    print(f"Día Lunes,  TURNO 4: LIBRE")
                else:
                    print(f"Día Lunes,  TURNO 4: {turno_lunes4}")
                if(turno_martes1==""):
                    print(f"Día Martes, TURNO 1: LIBRE")
                else:
                    print(f"Día Martes, TURNO 1: {turno_martes1}")
                if(turno_martes2==""):
                    print(f"Día Martes, TURNO 2: LIBRE")
                else:
                    print(f"Día Martes, TURNO 2: {turno_martes2}")
                if(turno_martes3==""):
                    print(f"Día Martes, TURNO 3: LIBRE")
                else:
                    print(f"Día Martes, TURNO 3: {turno_martes3}")
                input("\nPresione Enter para continuar... ")
            #OPCIÓN 4 - RESUMEN GENERAL
            case 4:
                print("\n----- RESUMEN GENERAL -----")
                #Verifica y suma los dias Lunes que se encuentres libres
                dias_libres_lunes =0
                if(turno_lunes1==""):
                    dias_libres_lunes +=1
                if(turno_lunes2==""):
                    dias_libres_lunes +=1
                if(turno_lunes3==""):
                    dias_libres_lunes +=1
                if(turno_lunes4==""):
                    dias_libres_lunes +=1
                dias_ocupados_lunes = 4 - dias_libres_lunes #Se hace la resta entre los dias totales y los libres
                
                #Verifica y suma los dias Martes que se encuentres libres
                dias_libres_martes =0
                if(turno_martes1==""):
                    dias_libres_martes +=1
                if(turno_martes2==""):
                    dias_libres_martes +=1
                if(turno_martes3==""):
                    dias_libres_martes +=1
                ddias_ocupados_martes = 3 - dias_libres_martes #Se hace la resta entre los dias totales y los libres
                
                print(f"\nEl dia Lunes tiene {dias_ocupados_lunes} turnos ocupados y {dias_libres_lunes} Disponibles")
                print(f"El dia Martes tiene {ddias_ocupados_martes} turnos ocupados y {dias_libres_martes} Disponibles\n")
                if(dias_ocupados_lunes > ddias_ocupados_martes):
                    print("El día con más turnos ocupados es el LUNES.\n")
                elif(dias_ocupados_lunes == ddias_ocupados_martes):
                    print("Ambos días tienen la misma cantidad de turnos ocupados (empate).\n")
                else:
                    print("El día con más turnos ocupados es el MARTES.\n")

                input("\nPresione Enter para continuar... ")
            #Se ejecuta si el número de opcion esta fuera del rango establecido entre 1 y 5
            case 5:
                break
            case _:
                print("ERROR: opción fuera de rango.\n")
                
    print("\n<----- MENU DE OPCIONES ------>\n")
    print("1) Reservar turno\n2) Cancelar turno (por nombre)\n3) Ver agenda del día\n4) Ver resumen general\n5) Cerrar sistema\n<---------------------------->\n")
    opcion= input("¿Que desea realizar? OPCIÓN: ")
print("\nGracias por utilizar el programa... Hasta Luego!!!")
input("\nPresione Enter para continuar... ")