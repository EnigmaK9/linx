import numpy as np
import random
import math
import csv
import matplotlib.pyplot as plt

# Constantes
RADIO_TIERRA = 6371000  # Metros
DISTANCIA_PERIHELIO = 147.1e6  # Kilómetros
IRRADIANCIA_PERIHELIO = 1367  # W/m^2 (constante solar promedio)
CAPACIDAD_BATERIA = 6000  # mAh (Capacidad de la batería de iones de litio)

# Parámetros del sistema
BATERIA_MAX = CAPACIDAD_BATERIA  # mAh
BATERIA_MIN = 2000.0  # mAh
CONSUMO_CAMARA = 115.0  # mAh/hora (consumo en mAh)
CONSUMO_DETECTOR_PARTICULAS = 288.0  # mAh/hora (consumo en mAh)
CONSUMO_BAJADA_DATOS = 1080.0  # mAh/hora (consumo en mAh)
CONSUMO_SUBIDA_DATOS = 144  # mAh/hora (consumo en mAh)
DEGRADACION_BATERIA = 0.01  # % por hora
CONSUMO_OBC = 2880  # % por hora
bateria_inicial = CAPACIDAD_BATERIA  # mAh

# Parámetros del panel solar
AREA_PANEL = 0.4  # m²
EFICIENCIA_PANEL = 0.25  # %

# Definición de las tareas
TAREAS = {
    "camara": {
        "id": 1,
        "consumo": CONSUMO_CAMARA,
        "duracion": 216.0 / 60.0,  # horas
    },
    "espectometro": {
        "id": 2,
        "consumo": CONSUMO_DETECTOR_PARTICULAS,
        "duracion": 8.0,  # horas
    },
    "bajada_datos": {
        "id": 3,
        "consumo": CONSUMO_BAJADA_DATOS,
        "duracion": 216 / 60,  # horas
    },
    "subida_datos": {
        "id": 4,
        "consumo": CONSUMO_SUBIDA_DATOS,
        "duracion": 24,  # horas
    },
    "OBC": {
        "id": 5,
        "consumo": CONSUMO_OBC,
        "duracion": 24,  # horas
    }
}

# Función para calcular el consumo de energía de una tarea
def calcular_consumo(tarea, tiempo):
    return tarea["consumo"] * tiempo / 60.0  # Convertir de mAh/hora a mAh/minuto
# comentario para mostrar que se actualia
# Función para actualizar el estado de la batería
def actualizar_bateria(bateria, consumo, carga):
    nueva_bateria = bateria - consumo + carga
    return max(min(nueva_bateria, BATERIA_MAX), BATERIA_MIN)

# Función para tomar una decisión sobre la activación de una tarea
def tomar_decision(bateria, orbita, tarea):
    # TODO: Implementar el algoritmo de aprendizaje por refuerzo
    return random.random() > 0.5

# Función para calcular la carga solar
def calcular_carga_solar(altura, tiempo):
    # Calcular la distancia entre el satélite y el sol (aproximadamente constante para simplificar)
    distancia = RADIO_TIERRA + altura

    # Utilizamos la ley de los inversos del cuadrado de la distancia
    irradiancia = IRRADIANCIA_PERIHELIO * (DISTANCIA_PERIHELIO / distancia) ** 2

    # Parámetros de la función sigmoide
    a = 0.5 * irradiancia * AREA_PANEL * EFICIENCIA_PANEL  # Máxima potencia alcanzable
    b = 0  # Mínima potencia
    c = 0.01  # Pendiente de la curva sigmoide
    d = 720  # Punto medio de la curva sigmoide (la mitad del tiempo total)
    
    # Función sigmoide para modelar el aumento gradual de la potencia
    potencia_generada = a / (1 + math.exp(-c * (tiempo - d))) + b
    
    return potencia_generada

# Función para simular una órbita
def simular_orbita(bateria, orbita, altura, tiempo_orbita):
    decisiones = []

    for tarea in TAREAS.values():
        if tarea["id"] == 3 and orbita == 0:
            # Bajar datos solo en la primera órbita
            decision = True
        else:
            decision = tomar_decision(bateria, orbita, tarea)

        if decision:
            consumo = calcular_consumo(tarea, tarea["duracion"])
            bateria -= consumo

        decisiones.append(int(decision))

    carga_solar = calcular_carga_solar(altura, orbita * tiempo_orbita)
    bateria = actualizar_bateria(bateria, 0, carga_solar)

    return bateria, decisiones

# Simulación principal
bateria = bateria_inicial  # mAh
altura_orbita = 500000  # Metros
numero_orbitas = 15
tiempo_orbita = 90.0  # minutos

# Lista para almacenar el estado de la batería
bateria_historico = [bateria]

# Lista para almacenar la carga solar por órbita
carga_solar_historico = []

for orbita in range(numero_orbitas):
    bateria, decisiones = simular_orbita(bateria, orbita, altura_orbita, tiempo_orbita)
    bateria_historico.append(bateria)
    carga_solar_historico.append(calcular_carga_solar(altura_orbita, orbita * tiempo_orbita))

    # Imprimir información de la órbita
    print(f"Órbita {orbita + 1}:")
    print(f" - Batería: {bateria:.2f} mAh ({bateria / BATERIA_MAX * 100:.2f}%)")
    print(f" - Carga solar: {carga_solar_historico[-1]:.2f} mAh")
    print(f" - Decisiones: {decisiones}")

# Graficar el estado de la batería
plt.plot(range(numero_orbitas + 1), bateria_historico)
plt.xlabel("Órbita")
plt.ylabel("Batería (mAh)")
plt.grid(True)
plt.show()

# Graficar la carga solar
plt.plot(range(numero_orbitas), carga_solar_historico)
plt.xlabel("Órbita")
plt.ylabel("Carga solar (mAh)")
plt.grid(True)
plt.show()

# Calcular el consumo total de energía
consumo_total = sum(calcular_consumo(tarea, tarea["duracion"]) for tarea in TAREAS.values())

# Calcular la vida útil de la batería
vida_util = bateria_inicial / consumo_total

# Calcular la eficiencia energética
eficiencia = (bateria_inicial - consumo_total) / consumo_total

# Imprimir los resultados
print(f"Consumo total de energía: {consumo_total:.2f} mAh")
print(f"Vida útil de la batería: {vida_util:.2f} órbitas")
print(f"Eficiencia energética: {eficiencia:.2f}%")
