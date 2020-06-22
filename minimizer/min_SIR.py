import numpy as np
from scipy.integrate import odeint
from scipy.optimize import minimize

from libs.fct_erreur import erreur
import data as dt


### Fonctions ###

# Les équations différentielles du modèle SIR.
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

def minimisation_SIR(coeff, observations, init_cond, N):
    t = np.arange(0, len(observations))
    ret = odeint(deriv, init_cond, t, args=(N, coeff[0], coeff[1]))
    S, I, R = ret.T
    C = np.zeros(len(I))
    C[0] = I[0]
    for i in range(0, len(I)):
        C[i] = C[i - 1] + I[i]
    return erreur(observations, C)


### Paramètres ###

# Population totale.
N = 64081000
# Nombre initial d'individus infectés et guéris.
I0, R0 = 2, 0
# Nombre d'individu susceptibles d'attrapper la maladie.
S0 = N - I0 - R0

# Vecteur des conditions initiales.
y0 = S0, I0, R0


resultat = minimize(minimisation_SIR, np.array([9.13370681, 9.01266501]), args=(dt.France_C[2:], y0, N))
print(resultat)
