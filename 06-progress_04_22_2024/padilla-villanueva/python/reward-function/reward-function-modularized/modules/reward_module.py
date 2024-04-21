import numpy as np

def calculate_reward(S_j, P_j, t_j_E, t_j_R, sigma, P_j_D, d_j, g_k):
    """
    Calculate the reward for a single event based on various event parameters.

    Parameters:
    - S_j (float): Stability factor of the event.
    - P_j (float): Power consumption of the event.
    - t_j_E (float): Expected time of the event.
    - t_j_R (float): Realized time of the event.
    - sigma (float): Standard deviation for time calculation.
    - P_j_D (float): Power drain during the event.
    - d_j (float): Duration of the event.
    - g_k (float): Gain associated with the event.

    Returns:
    - float: Calculated reward for the given event.
    """
    time_factor = ((t_j_E - t_j_R) / sigma) ** 2
    return S_j * P_j * np.exp(time_factor) + (P_j_D * d_j * g_k)

