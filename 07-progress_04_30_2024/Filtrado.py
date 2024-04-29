"""
import numpy as np
import pandas as pd

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
    dfTraining['decisionFactor'] = (1 / dfTraining['power']) * (dfTraining['taskPriority'] + dfTraining['executionPriority'])

    # Normalize the decision factor and set a threshold to make execution decisions
    maxFactor = dfTraining['decisionFactor'].max()
    dfTraining['Execute'] = np.where(dfTraining['decisionFactor'] > maxFactor * 0.5, 1, 0)

    # Drop the decision factor column as it is no longer needed
    dfTraining = dfTraining.drop('decisionFactor', axis=1)

    return dfTraining

def save_dataframe_to_csv(dataframe, file_name):
    dataframe.to_csv(file_name, index=False)

# Generate synthetic data to train the model
dfTraining = generateSyntheticData(numSamples=1000, initialSoC=95)

# Filter the DataFrame to include only rows where 'Execute' column is 1
dfFiltered = dfTraining[dfTraining['Execute'] == 1]

# Save the filtered DataFrame to a CSV file
save_dataframe_to_csv(dfFiltered, 'synthetic_data_filtered.csv')

# Check the filtered data
print(dfFiltered.head(15))
"""

import numpy as np
import pandas as pd

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
    dfTraining['decisionFactor'] = (1 / dfTraining['power']) * (dfTraining['taskPriority'] + dfTraining['executionPriority'])

    # Normalize the decision factor and set a threshold to make execution decisions
    maxFactor = dfTraining['decisionFactor'].max()
    dfTraining['Execute'] = np.where(dfTraining['decisionFactor'] > maxFactor * 0.5, 1, 0)

    # Drop the decision factor column as it is no longer needed
    dfTraining = dfTraining.drop('decisionFactor', axis=1)

    return dfTraining

def save_dataframe_to_csv(dataframe, file_name):
    dataframe.to_csv(file_name, index=False)

def calculate_values(df):
    sigma = 1.5  # Assuming a value for sigma
    g_k = 1  # Assuming a value for g_k

    # Calculate the values using the formula provided
    df['calculated_values'] = df['Execute'] * df['executionPriority'] * np.exp(((df['initialTime'] - df['duration']) / sigma) ** 2) + (df['taskPriority'] * df['duration'] * g_k)

    return df

# Generate synthetic data to train the model
dfTraining = generateSyntheticData(numSamples=1000, initialSoC=95)

# Filter the DataFrame to include only rows where 'Execute' column is 1
dfFiltered = dfTraining[dfTraining['Execute'] == 1]

# Calculate the new values
dfFiltered = calculate_values(dfFiltered)

# Save the filtered and calculated DataFrame to a CSV file
save_dataframe_to_csv(dfFiltered, 'synthetic_data_filtered_calculated.csv')

# Check the filtered and calculated data
print(dfFiltered.head(15))
