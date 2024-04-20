import numpy as np
import pandas as pd  # Import pandas library

def generateSyntheticData(numSamples=1000, initialSoC=95):
    np.random.seed(42)  # For reproducibility
    initialTime = np.random.uniform(0, 100, numSamples)
    durations = np.random.uniform(1, 10, numSamples)
    power = np.random.uniform(1, 3, numSamples)
    taskPriority = np.random.uniform(0, 1, numSamples)
    executionPriority = np.random.uniform(0, 1, numSamples)

    dfTraining = pd.DataFrame({
        'initialTime': initialTime,
        'duration': durations,
        'power': power,
        'taskPriority': taskPriority,
        'executionPriority': executionPriority
    })

    # Decision factor based on power and priorities
    dfTraining['decisionFactor'] = (1 / dfTraining['power']) * (dfTraining['taskPriority']
    + dfTraining['executionPriority'])

    # Normalize the decision factor and set a threshold to make execution decisions
    maxFactor = dfTraining['decisionFactor'].max()

    # Column for execution decision based on the decision factor threshold
    dfTraining['Execute'] = np.where(dfTraining['decisionFactor'] > maxFactor * 0.5, 1, 0)

    # Drop the decision factor column as it is no longer needed
    dfTraining = dfTraining.drop('decisionFactor', axis=1)

    return dfTraining  # Return the DataFrame without the decision factor column

    # Generate synthetic data to train the model
    dfTraining = generateSyntheticData(numSamples=1000, initialSoC=95)

    # Check the data
    print(dfTraining.head(15))

    def save_dataframe_to_csv(dataframe, file_name):
        dataframe.to_csv(file_name, index=False)

    # Assuming 'dfTraining' is your DataFrame
    save_dataframe_to_csv(dfTraining,
                          '/home/enigma/repos/linx/06-project-progress_04_22_2024/carlos-padilla/python_insert_data/synthetic_data.csv')

