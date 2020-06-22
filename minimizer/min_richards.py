import numpy as np
from scipy.optimize import minimize

from libs.fct_erreur import erreur
import libs.models as md
import data as dt


### Fonctions ###


def minimisation_richards(coeff, observations, C0, K):
    t = np.arange(0, len(observations))
    C = md.richards(C0, K, coeff[0], t, coeff[1])
    return erreur(observations, C)



### Paramètres ###

# Nombre initial d'infectés
C0 = 2

# Nombre cumulatif final d'infectés
K = 189670

# Taux de croissance exponentielle
r = 0.17434972

# Coefficient
alpha = 1.0698869171667518

resultat = minimize(minimisation_richards, np.array([r, alpha]), args=(dt.France_C[2:], C0, K))
print(resultat)
