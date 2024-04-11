import numpy as np
import random

# Parámetros del sistema
BATERIA_MAX = 100.0  # Wh
BATERIA_MIN = 30.0  # Wh
CONSUMO_CAMARA = 10.0  # Wh/hora
CONSUMO_ESPECTROMETRO = 5.0  # Wh/hora
CONSUMO_BAJADA_DATOS = 20.0  # Wh/hora
CONSUMO_SUBIDA_DATOS = 5.0  # Wh/hora
DEGRADACION_BATERIA = 0.01  # % por hora

# Parámetros del panel solar
POTENCIA_PANEL = 5.0  # W
EFICIENCIA_PANEL = 0.2  # %

# Definición de las tareas
TAREAS = {
    "camara": {
        "id": 1,
        "consumo": CONSUMO_CAMARA,
        "duracion": 45.0 / 60.0,  # horas
    },
    "espectometro": {
        "id": 2,
        "consumo": CONSUMO_ESPECTROMETRO,
        "duracion": 1.0,  # horas
    },
    "bajada_datos": {
        "id": 3,
        "consumo": CONSUMO_BAJADA_DATOS,
        "duracion": 0.1,  # horas
    },
    "subida_datos": {
        "id": 4,
        "consumo": CONSUMO_SUBIDA_DATOS,
        "duracion": 0.1,  # horas
    },
}

# Función para calcular el consumo de energía de una tarea
def calcular_consumo(tarea, tiempo):
    return tarea["consumo"] * tiempo

# Función para actualizar el estado de la batería
def actualizar_bateria(bateria, consumo, carga):
    nueva_bateria = bateria - consumo + carga
    return max(nueva_bateria, BATERIA_MIN)

# Función para tomar una decisión sobre la activación de una tarea
def tomar_decision(bateria, orbita, tarea):
    # TODO: Implementar el algoritmo de aprendizaje por refuerzo

    return random.random() > 0.5

# Función para calcular la carga solar
def calcular_carga_solar(orbita, tiempo_orbita):
    # TODO: Implementar un modelo más preciso de la carga solar
    # Considerar la orientación del satélite, la posición del Sol, etc.

    return POTENCIA_PANEL * EFICIENCIA_PANEL * tiempo_orbita

# Función para simular una órbita
def simular_orbita(bateria, orbita, tiempo_orbita):
    decisiones = []
    carga_solar = calcular_carga_solar(orbita, tiempo_orbita)

    for tarea in TAREAS.values():
        if tarea["id"] == 3 and orbita == 0:
            # Bajar datos solo en la primera órbita
            decision = True
        else:
            decision = tomar_decision(bateria, orbita, tarea)

        if decision:
            bateria = actualizar_bateria(bateria, calcular_consumo(tarea, tarea["duracion"]), 0)

        decisiones.append(int(decision))

    bateria = actualizar_bateria(bateria, 0, carga_solar)

    return bateria, decisiones

# Simulación principal
bateria = 80.0  # Wh
numero_orbitas = 15
tiempo_orbita = 90.0 / 60.0  # horas

# Lista para almacenar el estado de la batería
bateria_historico = [bateria]

# Lista para almacenar la carga solar por órbita
carga_solar_historico = []

for orbita in range(numero_orbitas):
    bateria, decisiones = simular_orbita(bateria, orbita, tiempo_orbita)
    bateria_historico.append(bateria)
    carga_solar_historico.append(calcular_carga_solar(orbita, tiempo_orbita))

    # Imprimir información de la órbita
    print(f"Órbita {orbita + 1}:")
    print(f" - Batería: {bateria:.2f} Wh ({bateria / BATERIA_MAX * 100:.2f}%)")
    print(f" - Carga solar: {carga_solar_historico[-1]:.2f} Wh")
    print(f" - Decisiones: {decisiones}")

# Graficar el estado de la batería
import matplotlib.pyplot as plt

plt.plot(range(numero_orbitas + 1), bateria_historico)
plt.xlabel("Órbita")
plt.ylabel("Batería (Wh)")
plt.grid(True)
plt.show()

# Graficar la carga solar
plt.plot(range(numero_orbitas), carga_solar_historico)
plt.xlabel("Órbita")
plt.ylabel("Carga solar (Wh)")
plt.grid(True)
plt.show()

# Calcular el consumo total de energía
consumo_total = 0
for orbita in range(numero_orbitas):
    for tarea in TAREAS.values():
        decision = decisiones[orbita][tarea["id"] - 1]
        if decision:
            consumo_total += calcular_consumo(tarea, tarea["duracion"])

# Calcular la vida útil de la batería
vida_util = bateria_inicial / consumo_total

# Calcular la eficiencia energética
eficiencia = (bateria_inicial - bateria_final) / consumo_total

# Imprimir los resultados
print(f"Consumo total de energía: {consumo_total:.2f} Wh")
print(f"Vida útil de la batería: {vida_util:.2f} órbitas")
print(f"Eficiencia energética: {eficiencia:.2f}%") 