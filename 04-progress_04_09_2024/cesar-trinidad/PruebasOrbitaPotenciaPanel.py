#Cesar Trinidad
#Este programa establece la potencia generada por el panel solar durante un dia
#Se toma una funcion sigmoide para identificar el aumento con el paso del tiempo dependiendo el paso del tiempo

import math
import csv
import matplotlib.pyplot as plt

# Constantes
RADIO_TIERRA = 6371000  # Metros
DISTANCIA_PERIHELIO = 147.1e6  # Kilómetros
DISTANCIA_AFELIO = 152.1e6  # Kilómetros
IRRADIANCIA_PERIHELIO = 1367  # W/m^2 (constante solar promedio)

# Función para leer los datos de entrada del usuario
def leer_datos_usuario():
    altura = float(input("Introduzca la altura de la órbita (km): "))
    # Convertir la altura de km a metros (m)
    altura *= 1000
    # El área del panel solar se debe ajustar para ser realista
    area_panel = float(input("Introduzca el área del panel solar (m²): "))
    # Eficiencia típica de los paneles solares en el espacio (aproximadamente 25%)
    eficiencia = 0.25
    return altura, area_panel, eficiencia

# Función para calcular la irradiancia solar
def calcular_irradiancia_solar(distancia):
    # Utilizamos la ley de los inversos del cuadrado de la distancia
    return IRRADIANCIA_PERIHELIO * (DISTANCIA_PERIHELIO / distancia) ** 2

# Función sigmoide para modelar el aumento gradual de la potencia
def sigmoide(x, a, b, c, d):
    return a / (1 + math.exp(-c * (x - d))) + b

# Función para calcular la potencia generada por el panel solar
def potencia_generada(irradiancia, area_panel, eficiencia, tiempo):
    # Parámetros de la función sigmoide
    a = 0.5 * irradiancia * area_panel * eficiencia  # Máxima potencia alcanzable
    b = 0  # Mínima potencia
    c = 0.01  # Pendiente de la curva sigmoide
    d = 720  # Punto medio de la curva sigmoide (la mitad del tiempo total)
    return sigmoide(tiempo, a, b, c, d)

# Función para guardar los resultados en un archivo CSV
def guardar_resultados_csv(tiempo_utc, potencia_generada):
    with open("resultados.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Tiempo (UTC)", "Potencia generada (W)"])
        for i in range(len(tiempo_utc)):
            writer.writerow([tiempo_utc[i], potencia_generada[i]])

# Función para graficar la potencia generada durante el día
def graficar_potencia(tiempo_utc, potencia_generada):
    plt.plot(tiempo_utc, potencia_generada)
    plt.xlabel("Tiempo (minutos)")
    plt.ylabel("Potencia generada (W)")
    plt.title("Potencia generada por el panel solar durante el día")
    plt.show()

# Función principal
def main():
    # Leer los datos de entrada del usuario
    altura, area_panel, eficiencia = leer_datos_usuario()

    # Inicializar variables
    tiempo_utc = list(range(0, 1440, 5))  # Ciclo cada 5 minutos
    potencia_generada_list = []

    # Bucle para calcular la potencia durante un día
    for tiempo in tiempo_utc:
        # Calcular la distancia entre el satélite y el sol (aproximadamente constante para simplificar)
        distancia = RADIO_TIERRA + altura

        # Calcular la irradiancia solar
        irradiancia_solar = calcular_irradiancia_solar(distancia)

        # Calcular la potencia generada
        potencia_generada_list.append(potencia_generada(irradiancia_solar, area_panel, eficiencia, tiempo))

    # Guardar los resultados en un archivo CSV
    guardar_resultados_csv(tiempo_utc, potencia_generada_list)

    # Graficar la potencia generada durante el día
    graficar_potencia(tiempo_utc, potencia_generada_list)

# Ejecutar la función principal
if __name__ == "__main__":
    main()



