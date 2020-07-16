import numpy as np
from scipy.optimize import minimize

from libs.useful_fcts import error, richards_minimization
import libs.models as md
import data as dt


### Fonctions ###


def minimisation_richards(coeff, observations, C0, K):
    t = np.arange(2, len(observations) + 2)
    C = md.richards(C0, K, coeff[0], t, coeff[1])
    return error(observations, C)



### Paramètres ###

# Nombre initial d'infectés
C0 = 2

# Nombre cumulatif final d'infectés
K = 189670

# Taux de croissance exponentielle
r = 0.16942401

# Coefficient
alpha = 1.0685873

resultat = minimize(minimisation_richards, np.array([r, alpha]), args=(dt.France_C[2:], C0, K))
print(resultat)
print(richards_minimization(np.array([r, alpha]), (dt.France_C[2:], C0, K)))