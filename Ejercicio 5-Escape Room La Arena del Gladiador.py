import random

#VARIABLES INICIALES
vida_gladiador = 100
vida_enemigo = 100
pociones_vida = 3 
danio_base_gladiador = 15 
danio_base_enemigo = 12
turno_gladiador=True


#Ingreso del nombre con la validacíon de solo letras
nombre_gladiador=input("\nIngrese el nombre del gladiador: ")
while nombre_gladiador=="" or not nombre_gladiador.isalpha():
    print("Error: Solo se permiten letras")
    nombre_gladiador=input("Ingrese el nombre del gladiador: \n")
nombre_gladiador=nombre_gladiador.upper() 

#Comienzo del Ciclo While que corresponde a la contienda.
while vida_gladiador>0 and vida_enemigo>0:
    if turno_gladiador:
        print(f"\nVida de {nombre_gladiador} : |{vida_gladiador}| | VS | Vida del enemigo: |{vida_enemigo}| HP")
        print(f"Pociones de cura disponibles |{pociones_vida}|")
        if(vida_gladiador!=vida_enemigo):
            input("\nPresione Enter para continuar...")
        while True:
            #Ingreso de opción del menu y validación de si es solo digito
            opcion=input("\nIndique la accion a realizar: \n< " + '-'*30 + "> \n1) Ataque pesado \n2) Ataque por rafaga \n3) Curar \n < " + '-'*30 + ">\nElija OPCIÓN: ")
            while opcion=="" or not opcion.isdigit():
                print("Error: Solo se permiten numeros")
                opcion=input("\nIndique la accion a realizar: \n< " + '-'*30 + ">\n1) Ataque pesado \n2) Ataque por rafaga \n3) Curar \n < " + '-'*30 + ">\nElija OPCIÓN: ")
            opcion=int(opcion)
            match opcion:
                #1 - Proceso ataque PODER OCULTO
                case 1:
                    #Dependiendo de la vida del oponente, se resta la vida al mismo
                    if vida_enemigo<20:
                        vida_enemigo=vida_enemigo-1.5*danio_base_gladiador
                        print(f"\nAtacaste al enemigo por {1.5*danio_base_gladiador} puntos de daño")
                    else:
                        vida_enemigo=vida_enemigo-danio_base_gladiador
                        print(f"\nAtacaste al enemigo por {danio_base_gladiador} puntos de daño")
                    turno_gladiador=False
                    break
                #Proceso del Ataque Rafaga. El daño depende de un numero aleatorio entre 1 y 4
                case 2:
                    rafaga=random.randint(1,4)
                    for _ in range(rafaga):
                        vida_enemigo-=5
                        print("> Golpe conectado por 5 de daño")
                    turno_gladiador=False
                    break
                #Opcion de Curación: Se revisa si posee pociones y la cantidad de vida el personaje
                case 3:
                    if pociones_vida>0:
                        if(vida_gladiador==100):
                            print("Tienes la vida completa.... No se te descontará la poción pero pierdes UN TURNO")
                        elif(vida_gladiador>=70):
                            vida_gladiador = 100
                            pociones_vida-=1
                        else:
                            vida_gladiador=vida_gladiador+30
                            pociones_vida-=1
                            print(f"\nTe curaste, tu vida sube a {vida_gladiador}")
                        print(f"\n{pociones_vida} pociones de cura restantes.")
                    else:
                        print("\nNo dispone de mas pociones de vida")
                        print("Pierdes el turno\n")
                    turno_gladiador=False
                    break
                #Validación del ingreso de una opcion que no corresponde
                case _:
                    print("\nLa opcion ingresada no es valida")
                    print("Intente de nuevo")
    else:
        #Ataque automático del enemigo
        print("\nTurno de ataque del enemigo!!")
        vida_gladiador=vida_gladiador-danio_base_enemigo
        print("¡El enemigo te atacó por 12 puntos de daño!\n")
        turno_gladiador=True

#Resultado de la contienda. Victoria o Derrota
if vida_gladiador>0:
    print(f"¡VICTORIA! {nombre_gladiador} ha ganado la batalla.\n")
else:
    print(f"DERROTA. Has caído en combate.\n")


