import numpy as np
from scipy.optimize import minimize

from libs.fct_erreur import erreur
import libs.models as md
import data as dt


### Fonctions ###

def minimisation_logistique(coeff, observations, C0, K):
    t = np.arange(0, len(observations))
    C = md.logistique(C0, K, coeff, t)
    return erreur(observations, C)


### Paramètres ###

# Nombre initial d'infectés
C0 = 2

# Nombre cumulatif final d'infectés
K = 189670

# Taux de croissance exponentielle
r = 0.15011031

resultat = minimize(minimisation_logistique, np.array([r]), args=(dt.France_C[2:], C0, K))
print(resultat)
