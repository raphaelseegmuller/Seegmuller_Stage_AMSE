import numpy as np
from scipy.integrate import odeint
from scipy.optimize import minimize

from libs.useful_fcts import error, SIR_minimization
import data as dt


### Fonctions ###

# Les équations différentielles du modèle SIR.
def deriv_SIR(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

def minimisation_SIR(coeff, observations, init_cond, N):
    t = np.arange(2, len(observations)+2)
    ret = odeint(deriv_SIR, init_cond, t, args=(N, coeff[0], coeff[1]))
    S, I, R = ret.T
    C = np.zeros(len(I))
    C[0] = I[0]
    for i in range(0, len(I)):
        C[i] = C[i - 1] + I[i]
    return error(observations, C)


### Paramètres ###

# Population totale.
N = 64081000
# Nombre initial d'individus infectés et guéris.
I0, R0 = 2, 0
# Nombre d'individu susceptibles d'attrapper la maladie.
S0 = N - I0 - R0

# Vecteur des conditions initiales.
y0 = S0, I0, R0


resultat = minimize(minimisation_SIR, np.array([9.24884336, 9.12660313]), args=(dt.France_C[2:], y0, N))
print(resultat)
print(SIR_minimization(np.array([9.24884336, 9.12660313]), (dt.France_C[2:], y0, N)))