from modules.reward_module import calculate_reward
from modules.performance_module import overall_performance
import numpy as np

if __name__ == "__main__":
    # Example parameters
    S_j = 1
    P_j = 1
    t_j_E = 10
    t_j_R = 5
    sigma = 2
    P_j_D = 1
    d_j = 0.5
    g_k = 0.1

    reward = calculate_reward(S_j, P_j, t_j_E, t_j_R, sigma, P_j_D, d_j, g_k)

    alpha = 0.5
    E = np.array([0.1, 0.2, 0.3])
    E_L = 0.0
    E_max = 1.0

    overall_metric = overall_performance([reward], alpha, E, E_L, E_max)

    print("Value of individual reward:", reward)
    print("Value of overall performance:", overall_metric)

