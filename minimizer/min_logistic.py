from libs.useful_fcts import logistic_minimization
import numpy as np

'''
Pour lancer ce programme, le sortir du dossier minimizer.
'''

### Paramètres ###

# Pays
country = "France"

# Taux de croissance exponentielle
r = 0.10786183

print("Coefficient optimal = ", logistic_minimization(np.array([r]), country))
