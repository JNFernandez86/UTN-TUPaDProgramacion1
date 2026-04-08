#VARIABLES INICIADAS
intento=0

print("<------    BIENVENIDO    ------->")
print("<------ Ingreso al Campus ------>\n")
usuario = input("Ingrese Usuario: ")
password = input("Ingrese Contraseña: ")

#VERIFICA USUARIO Y CONTRASEÑA. LIMITA A 3 INTENTOS
while(intento<3):
    if(usuario=='alumno' and password=='python123'):
        print(f"Intento {intento+1}/3: ACCESO PERMITIDO\n")
        break
    else:
        intento+=1
        if(intento==3):
            break
        else:
            print(f"\nIntento {intento}/3 Credenciales Inválidas: Acceso Denegado\n")
            usuario = input("Ingrese de nuevo el Usuario: ")
            password = input("Ingrese de nuevo la Clave: ")
        
if(intento<3):    
    #MENU DE OPCIONES    
    print("<----- MENU ------>")
    print("1) Consultar Estado\n2) Cambiar Clave\n3) Mostrar mensaje motivacional\n4) SALIR\n")
    opcion= input("¿Que desea realizar? OPCIÓN: ")
    #CONDICION PARA SALIR DEL BUCLE =4
    while(opcion!='4'):
        while(opcion.isdigit()== False):
            opcion= input("\nERROR: INGRESE UN NÚMERO VÁLIDO: ")
        match int(opcion):
            #OPCIÓN 1: MUESTRA ESTADO DE INSCRIPCIÓN
            case 1: 
                print("\nSu estado de Inscripción es: INSCRIPTO\n")
            # OPCIÓN 2: OPERACION DE CAMBIO DE CONTRASEÑA
            case 2:
                print("\nSeleccionó Cambio de contraseña...")
                claveNueva= input("\nIngrese la nueva contraseña: ")
                while(len(claveNueva)<6):#VERIFICA LONGITUD MINIMA DE CARACTERES PARA LA NUEVA CONTREÑA
                    print("\nLa contraseña debe tener mínimo 6 caracteres")
                    claveNueva=input("\nVuelva a ingresar la nueva contraseña: ")
                verificarNuevaClave=input("Vuelva a escribir la contraseña para validar: ")
                while(verificarNuevaClave != claveNueva): #VERIFICA SI LAS CONTRASEÑAS COINCIDEN (NUEVA Y V) 
                    print("\nLas contraseñas no coinciden.")
                    verificarNuevaClave = input("\nIngrese nuevamente la clave para validarla: ")
                print("\nContraseña ha sido modificada con éxito!!\n")            
            case 3:
                # OPCIÓN 3: MUESTRA FRASE MOTIVADORA
                print("\n##### NO TENGAS MIEDO DE FALLAR, TEN MIEDO DE NO INTENTARLO #####\n")
            case 4:
                #OPCIN SALIR
                break
            case _: #ARROJA ERROR SI LA OPCIÓN ES MAYOR QUE 4
                print("ERROR: opción fuera de rango.")
        print("<----- MENU ------>")
        print("1) Consultar Estado\n2) Cambiar Clave\n3) Mostrar mensaje motivacional\n4) SALIR\n")
        opcion= input("¿Qué desea realizar ahora? OPCIÓN: ")
else:
    #SALIDAD DE CONTRASEÑA INVALIDA POR 3 VECES
    print(f"\nIntento {intento}/3, Credenciales Inválidas: Acceso Denegado\n")
    print("¡¡¡SU USUARIO HA SIDO BLOQUEADO!!!. Comuniquese a soporte@campusutn.com para reestablecer su contraseña\n")

#MENSAJE DE FINALIZACIÓN
print("\nSESION CERRADA, HASTA PRONTO\n")
input("Presione cualquier tecla para finalizar")