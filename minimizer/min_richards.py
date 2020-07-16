from libs.useful_fcts import richards_minimization
import numpy as np

'''
Pour lancer ce programme, le sortir du dossier minimizer.
'''

### Paramètres ###

# Pays
country = "France"

# Taux de croissance exponentielle
r = 0.12764188

# Coefficient
alpha = 1.0732281

print("Coefficients optimaux = ", richards_minimization(np.array([r, alpha]), country))
