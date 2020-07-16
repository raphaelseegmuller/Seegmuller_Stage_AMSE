import numpy as np
from scipy.integrate import odeint


### Modèle logistique ###

def logistique(C0, K, r, t):
    """
    Calcul du nombre cumulé de cas de COVID 19 avec le modèle logistique.
    :param C0: int
    :param K: int
    :param r: int, float, numpy.ndarray
    :param t: list, numpy.ndarray
    :return: numpy.ndarray
    """
    C = np.zeros((len(t)))
    for d in range(len(t)):
        C[d] = (K * C0) / (C0 + (K - C0) * np.exp(-r * t[d]))
    return C


### Modèle de Richards ###

def richards(C0, K, r, t, alpha):
    """
    Calcul du nombre cumulé de cas de COVID 19 avec le modèle logistique.
    :param C0: int
    :param K: int
    :param r: int, float, numpy.ndarray
    :param t: list, numpy.ndarray
    :param alpha: float
    :return: numpy.ndarray
    """
    C = np.zeros((len(t)))
    for d in range(len(t)):
        C[d] = (K * C0) / (
                C0 ** alpha + (K ** alpha - C0 ** alpha) * np.exp(
            (-r * t[d] * (K ** alpha)) / (K ** alpha - C0 ** alpha)) ** (1 / alpha))
    return C


### Modèle SIR ###

# Les équations différentielles du modèle SIR.
def deriv_SIR(y, t, N, beta, gamma):
    """
    Définition des dérivées temporelles de S, I et R.
    :param y: tuple
    :param t: list, numpy.ndarray
    :param N: int
    :param beta: float
    :param gamma: float
    :return: tuple
    """
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt


def SIR(S_init, I_init, R_init, t, N_tot, beta, gamma):
    """
    Calcul du nombre cumulé de cas de COVID 19 avec le modèle SIR.
    :param S_init: int, float
    :param I_init: int, float
    :param R_init: int, float
    :param t: list, numpy.ndarray
    :param N_tot: int
    :param beta: float
    :param gamma: float
    :return: numpy.ndarray
    """
    # Vecteur des conditions initiales.
    y0 = S_init, I_init, R_init

    # Intégration des équations du modèle SIR.
    ret = odeint(deriv_SIR, y0, t, args=(N_tot, beta, gamma))
    I, R = ret.T[1], ret.T[2]

    # Nombre cumulé d'infectés.
    C = np.zeros(len(I))
    # C[0] = I[0]
    # for i in range(1, len(I)):
    #     C[i] = C[i - 1] + I[i]
    for i in range(len(I)):
        C[i] = I[i] + R[i]
    return C


### Modèle SEIR ###

# Les équations différentielles du modèle SEIR.
def deriv_SEIR(y, t, N, beta, sigma, gamma):
    """
    Définition des dérivées temporelles de S, E, I et R.
    :param y: tuple
    :param t: list, numpy.ndarray
    :param N: int
    :param beta: float
    :param sigma: float
    :param gamma: float
    :return: tuple
    """
    S, E, I, R = y
    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - sigma * E
    dIdt = sigma * E - gamma * I
    dRdt = gamma * I
    return dSdt, dEdt, dIdt, dRdt


def SEIR(S_init, E_init, I_init, R_init, t, N_tot, beta, sigma, gamma):
    """
    Calcul du nombre cumulé de cas de COVID 19 avec le modèle SEIR.
    :param S_init: int, float
    :param E_init: int, float
    :param I_init: int, float
    :param R_init: int, float
    :param t: list, numpy.ndarray
    :param N_tot: int
    :param beta: float
    :param sigma: float
    :param gamma: float
    :return: numpy.ndarray
    """
    # Vecteur des conditions initiales.
    y0 = S_init, E_init, I_init, R_init

    # Intégration des équations du modèle SIR.
    ret = odeint(deriv_SEIR, y0, t, args=(N_tot, beta, sigma, gamma))
    E, I, R = ret.T[1], ret.T[2], ret.T[3]

    # Nombre cumulé d'infectés.
    C = np.zeros(len(I))
    # C[0] = I[0]
    # for i in range(1, len(I)):
    #     C[i] = C[i - 1] + I[i]
    for i in range(len(I)):
        C[i] = E[i] + I[i] + R[i]
    return C
