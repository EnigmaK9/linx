from datetime import datetime, timedelta
import random
import matplotlib.pyplot as plt

import random

def asignar_valor_aleatorio():
    # Lista de valores posibles
    valores_posibles = [5, 3.3]
    
    # Asignar aleatoriamente un valor de la lista
    valor_asignado_Vop = random.choice(valores_posibles)
    
    return valor_asignado_Vop
print (asignar_valor_aleatorio())

#Parametros Antenas
potencia_COMS2408TX = 25 #En Watts
Vop_COMS2408TX = asignar_valor_aleatorio() #En Volts
corriente_COMS2408TX = (potencia_COMS2408TX / Vop_COMS2408TX) 
ciclos_de_trabajo = 15
tiempo_completo = 24
cilcos_de_trabajo_horas = ((ciclos_de_trabajo * tiempo_completo)/100)

def generar_hora_inicio_aleatoria():
    # Generar una hora aleatoria entre las 00:00 y las 23:59
    hora = random.randint(0, 23)
    minutos = random.randint(0, 59)
    segundos = random.randint(0, 59)
    return hora, minutos, segundos

def generar_tiempo_aleatorio():
    # Generar minutos aleatorios entre 0 y 59 
    minutos = random.randint(0, 59)
    # Generar segundos aleatorios entre 0 y 59
    segundos = random.randint(0, 59)
    return minutos, segundos

def formato_tiempo(minutos, segundos):
    return "{:02d}:{:02d}".format(minutos, segundos)

# Función para convertir tiempo a timedelta
def tiempo_a_timedelta(minutos, segundos):
    return timedelta(minutes=minutos, seconds=segundos)

def generar_lista_horas_y_tiempos(num_elementos, fecha):
    lista_horas_tiempos = []
    tiempo_total = timedelta()
    while tiempo_total.total_seconds() < 3.6 * 3600 and len(lista_horas_tiempos) < num_elementos:
        hora_inicio = generar_hora_inicio_aleatoria()
        minutos, segundos = generar_tiempo_aleatorio()
        tiempo = tiempo_a_timedelta(minutos, segundos)
        if tiempo_total + tiempo <= timedelta(hours=3, minutes=36):
            lista_horas_tiempos.append((fecha, hora_inicio, tiempo))
            tiempo_total += tiempo
    return lista_horas_tiempos

# Número de elementos en la lista que deseas generar
num_elementos = 5

# Crear una lista para almacenar los próximos 14 días
lista_14_dias = []

# Obtener la fecha actual
fecha_actual = datetime.now().date()

# Crear listas para almacenar hora_inicio y corriente_mAs
horas_inicio = []
corrientes_mAs = []

# Iterar sobre los próximos 14 días y agregarlos a la lista
days = 1
for i in range(days):
    fecha = fecha_actual + timedelta(days=i)
    lista_14_dias.append(fecha)

# Generar la lista de horas de inicio y tiempos aleatorios para cada día
for fecha in lista_14_dias:
    lista_horas_tiempos = generar_lista_horas_y_tiempos(num_elementos, fecha)
    
    # Imprimir la lista de fechas, horas de inicio y tiempos
    for i, (fecha, hora_inicio, tiempo) in enumerate(lista_horas_tiempos, 1):
        asignar_valor_aleatorio()
        Vop_COMS2408TX = asignar_valor_aleatorio() #En Volts
        print(Vop_COMS2408TX) #Para saber que valor de la corriente le esta dando
        corriente_COMS2408TX = (potencia_COMS2408TX / Vop_COMS2408TX) 
        corriente_mAs = round((tiempo.seconds * corriente_COMS2408TX), 2)

        # Almacenar los valores de hora_inicio y corriente_mAs en las listas
        horas_inicio.append(hora_inicio[0])  # Solo necesitamos la hora de inicio
        corrientes_mAs.append(corriente_mAs)

        print("Elemento {}: Fecha: {}, Hora de inicio: {}, Tiempo: {}, Corriente: {} mAs".format(i, fecha.strftime("%Y-%m-%d"),
        formato_tiempo(hora_inicio[0], hora_inicio[1]),
        formato_tiempo(tiempo.seconds // 60, tiempo.seconds % 60),
        corriente_mAs))

# Graficar el estado de la batería
import matplotlib.pyplot as plt

# Graficar el estado de la batería como una gráfica de dispersión
plt.scatter(horas_inicio, corrientes_mAs)
plt.title("Estado de la Batería")
plt.xlabel("Hora de inicio")
plt.ylabel("Corriente (mAs)")
plt.grid(True)
plt.show()