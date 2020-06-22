import numpy as np
from scipy.integrate import odeint
from scipy.optimize import minimize

from libs.fct_erreur import erreur
import data as dt


### Fonctions ###

# Les équations différentielles du modèle SEIR.
def deriv_SEIR(y, t, N, beta, sigma, gamma):
    S, E, I, R = y
    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - sigma * E
    dIdt = sigma * E - gamma * I
    dRdt = gamma * I
    return dSdt, dEdt, dIdt, dRdt

def minimisation_SEIR(coeff, observations, init_cond, N):
    t = np.arange(0, len(observations))
    ret = odeint(deriv_SEIR, init_cond, t, args=(N, coeff[0], coeff[1], coeff[2]))
    S, E, I, R = ret.T
    C = np.zeros(len(I))
    C[0] = I[0]
    for i in range(0, len(I)):
        C[i] = C[i - 1] + I[i]
    return erreur(observations, C)


### Paramètres ###

# Population totale.
N = 64081000
# Nombre initial d'individus infectés, infectieux et guéris.
E0, I0, R0 = 0, 2, 0
# Nombre d'individu susceptibles d'attrapper la maladie.
S0 = N - E0 - I0 - R0

# Vecteur des conditions initiales.
y0 = S0, E0, I0, R0


resultat = minimize(minimisation_SEIR, np.array([44.37642256, 2.74638698, 41.72459742]), args=(dt.France_C[2:], y0, N))
print(resultat)