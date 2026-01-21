import  numpy as np
from scipy.optimize import minimize_scalar

def compute_q(p):
    V = np.zeros((5, 4))
    V[4, :] = 1.0
    V[:, 3] = 0.0
    x = np.zeros((4, 3))

    for b in range(3, -1, -1):
        for s in range(2, -1, -1):
            Vb = V[b + 1, s]
            Vs = V[b, s + 1]
            delta = Vb - Vs
            denom = p * (4 - Vs) + delta
            x[b, s] = delta / denom if denom > 1e-12 and delta > 0 else 0
            V[b, s] = x[b, s] * Vs + (1 - x[b, s]) * Vb

    P = np.zeros((4, 3))
    P[0, 0] = 1.0

    for s in range(3):
        for b in range(4):
            if b > 0:
                x_prev = x[b - 1, s]
                P_B = (1 - x_prev) ** 2
                P[b, s] += P[b - 1, s] * P_B
            if s > 0:
                x_prev = x[b, s - 1]
                P_hr = p * x_prev ** 2
                P_B = (1 - x_prev) ** 2
                P_S = 1 - P_B - P_hr
                P[b, s] += P[b, s - 1] * P_S

    return P[3, 2]

# Optimize
res = minimize_scalar(lambda p: -compute_q(p), bounds=(0,1), method='bounded')
max_q = -res.fun
p_opt = res.x