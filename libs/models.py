import numpy as np
from scipy.integrate import odeint

### Modèle logistique ###

def logistique(C0, K, r, t):
    C = np.zeros((len(t)))
    for d in range(len(t)):
        C[d] = (K * C0) / (C0 + (K - C0) * np.exp(-r * t[d]))
    return C


### Modèle de Richards ###

def richards(C0, K, r, t, alpha):
    C = np.zeros((len(t)))
    for d in range(len(t)):
        C[d] = (K * C0) / (
                C0 ** alpha + (K ** alpha - C0 ** alpha) * np.exp(
            (-r * t[d] * (K ** alpha)) / (K ** alpha - C0 ** alpha)) ** (1 / alpha))
    return C


### Modèle SIR ###

# Les équations différentielles du modèle SIR.
def deriv_SIR(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt


def SIR(S_init, I_init, R_init, t, N_tot, beta, gamma):
    # Vecteur des conditions initiales.
    y0 = S_init, I_init, R_init

    # Intégration des équations du modèle SIR.
    ret = odeint(deriv_SIR, y0, t, args=(N_tot, beta, gamma))
    I = ret.T[1]

    # Nombre cumulé d'infectés.
    C = np.zeros(len(I))
    C[0] = I[0]
    for i in range(1, len(I)):
        C[i] = C[i - 1] + I[i]
    return C
