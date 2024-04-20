def generateSintheticData(numSampling=1000, initialSoC=95):
    np.random.seed(42)  # Para reproducibilidad
    initialTime = np.random.uniform(0, 100, numSampling)
    Durations = np.random.uniform(1, 10, numSampling)
    Powers = np.random.uniform(1, 3, numSampling)
    PriorityTs = np.random.uniform(0, 1, numSampling)
    PriorityEs = np.random.uniform(0, 1, numSampling)

    dfEntrenamiento = pd.DataFrame({
        'HoraInicio': initialTime,
        'Duracion': Durations,
        'Potencia': Powers,
        'PriorityT': PriorityTs,
        'PriorityE': PriorityEs
    })

# Generate sinthetic data to train model
dfTraining = generateSintheticData(numSampling=1000, initialSoC=95)

# check data
print(dfTraining.head())

