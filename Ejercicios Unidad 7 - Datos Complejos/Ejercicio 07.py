# 7)

# Dada una lista de empleados que asistieron a una reunión, crea un conjunto para identificar a los empleados únicos 
# y luego cuenta cuántas veces asistió cada empleado.
lista_asistencia = ["Carlos", "Ana", "Luis", "Carlos", "Ana", "Maria", "Luis","Pedro", "Maria", "Ana"]

conjunto_asistencia = set(lista_asistencia) # Crear un conjunto para identificar empleados únicos
print("Empleados que asistieron al menos una vez:")
print(conjunto_asistencia)

# Contar cuántas veces asistió cada empleado
print("\nCantidad de asistencias por empleado:")
for empleado in conjunto_asistencia:
    cantidad = lista_asistencia.count(empleado)
    print(f"{empleado}: {cantidad} vez/veces.")