# 9)

import datetime

def verificar_dia(dia):
    dias_validos = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    while True:
        if dia.capitalize() in dias_validos:
            return dia.capitalize()
        else:
            print("Ingrese un día válido (Lunes, Martes, Miércoles, Jueves, Viernes, Sábado o Domingo)")
            dia = input("Ingrese el día para consultar la agenda: ")

def verificar_hora(hora):
    while True:
        if len(hora) == 5 and hora[2] == ":":
            datetime.datetime.strptime(hora, "%H:%M")
            return hora
        else:
            print("Ingrese una hora válida en formato HH:MM (por ejemplo, 14:30)")
            hora = input("Ingrese la hora para consultar la agenda (formato HH:MM): ")

agenda = {
    ("Lunes","10:00"):"Clase de Yoga",
    ("Lunes","11:30"):"Parcial Programación I",
    ("Martes","09:00"):"Reunión Sprint",
    ("Martes","14:00"):"Clase de Inglés",
    ("Miércoles","16:00"):"Cita con el médico",
    ("Jueves","18:00"):"Cena con amigos",
    ("Jueves","14:00"):"Reunión seguimiento proyecto",
    ("Viernes","20:00"):"Película en casa" }

dia = input("Ingrese el día para consultar la agenda: ").capitalize()
dia = verificar_dia(dia)
hora = input("Ingrese la hora para consultar la agenda (formato HH:MM): ")
hora = verificar_hora(hora)
evento = agenda.get((dia, hora))
if evento:
    print(f"El evento programado para el {dia} a las {hora} es: {evento}")
else:
    print(f"No hay eventos programados para el {dia} a las {hora}.")
