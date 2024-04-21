import numpy as np

def overall_performance(rewards, alpha, E, E_L, E_max):
    """
    Calculate the overall performance metric for the system using individual event rewards and battery performance.

    Parameters:
    - rewards (list of float): Individual rewards from various events.
    - alpha (float): Coefficient for weighting battery performance.
    - E (numpy.array): Current energy levels of the system's batteries.
    - E_L (float): Lower energy threshold.
    - E_max (float): Maximum energy capacity.

    Returns:
    - float: Total performance metric calculated.
    """
    J = len(rewards)
    N = len(E)
    sum_rewards = np.sum(rewards)
    normalized_battery_performance = np.sum((E - E_L) / (E_max - E_L))
    return sum_rewards + (alpha / N) * normalized_battery_performance

