#4)


def validar_cadena(cadena): # Función para verificar si la cadena está vacía
    if cadena == "" and cadena.isalpha() == False and cadena.isdigit() == False:
        print("La cadena no puede estar vacía y debe contener solo letras o números.")
        return False
    else:
        return True
agenda = {}


for x in range(5): # Repetir el proceso 5 veces para agregar 5 personas a la agenda
    usuario = input("\nIngrese el nombre de la persona que desea agregar: ").capitalize()
    if not validar_cadena(usuario):
        continue
    telefono = input(f"Ingrese el número telefónico de {usuario}: ")
    if not validar_cadena(telefono):
        continue
    agenda[usuario] = telefono
    
buscar_nombre = input("\nIngrese el nombre que desea buscar: ").capitalize()
# Verificar si el nombre ingresado se encuentra en la agenda y mostrar su número telefónico
while True:
    
    validar_cadena(buscar_nombre)
    if buscar_nombre in agenda:
        print(f"\nEl número de {buscar_nombre} es: {agenda[buscar_nombre]}")
    else:
        print("El nombre no se encuentra en la agenda.")
    respuesta = input("\n¿Desea buscar otro nombre? (s/n): ").lower()
    if respuesta == "s":
        buscar_nombre = input("\nIngrese el nombre que desea buscar: ").capitalize()
    else:
        print("¡Hasta luego!")
        break
