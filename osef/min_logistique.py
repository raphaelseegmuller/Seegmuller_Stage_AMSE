from libs.useful_fcts import error, logistic_minimization
import libs.models as md
import numpy as np
from scipy.optimize import minimize

import data as dt


### Fonctions ###

def minimisation_logistique(coeff, observations, C0, K):
    t = np.arange(2, len(observations) + 2)
    C = md.logistique(C0, K, coeff, t)
    return error(observations, C)


### Paramètres ###

# Nombre initial d'infectés
C0 = 2

# Nombre cumulatif final d'infectés
K = 189670

# Taux de croissance exponentielle
r = 0.14628805

resultat = minimize(minimisation_logistique, np.array([r]), args=(dt.France_C[2:], C0, K))
print(resultat)


# def minimisation_logistique_bis(coeff, observations, C0, K):
#     # histoire de starting point CC
#     starting_point = 2
#     t = np.arange(2, len(observations) +2)
#     C = md.logistique(C0, K, coeff, t)



def minimisation(f, coeff, others):
    return minimize(f, coeff, args=others)

print(minimisation(minimisation_logistique, np.array([r]), (dt.France_C[2:], C0, K)).x)
print(logistic_minimization(np.array([r]), (dt.France_C[2:], C0, K)))