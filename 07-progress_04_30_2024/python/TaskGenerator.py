import numpy as np
import pandas as pd

# Generar datos sintéticos
def generarDatosSinteticos(numMuestras=10):
    np.random.seed(42)  # Para reproducibilidad
    HorasInicio = np.random.randint(0, 24, numMuestras)  # Generar horas aleatorias entre 0 y 23
    MinutosInicio = np.random.randint(0, 60, numMuestras)  # Generar minutos aleatorios entre 0 y 59
    MinutosDuracion = np.random.randint(0, 15, numMuestras)
    SegundosDuracion = np.random.randint(0, 60, numMuestras)
    Potencias = np.round(np.random.uniform(1, 3, numMuestras), 2)
    PriorityEs = np.round(np.random.uniform(0, 1, numMuestras), 2)
    PriorityDs = np.round(np.random.uniform(0, 1, numMuestras), 2)

    # Concatenar horas y minutos para formar un formato de tiempo más completo (HH:MM)
    TiempoInicio = [f"{hora:02d}:{minuto:02d}" for hora, minuto in zip(HorasInicio, MinutosInicio)]
    Duraciones = [f"{minuto:02d}:{segundos:02d}" for minuto, segundos in zip(MinutosDuracion, SegundosDuracion)]
    dfEntrenamiento = pd.DataFrame({
        'HoraInicio': TiempoInicio,
        'Duracion': Duraciones,
        'Potencia': Potencias,
        'PriorityE': PriorityEs,
        'PriorityD': PriorityDs
    })

    return dfEntrenamiento

# Generar datos
df = generarDatosSinteticos()
print(df)

