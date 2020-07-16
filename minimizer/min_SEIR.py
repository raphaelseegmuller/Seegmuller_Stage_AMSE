from libs.useful_fcts import SEIR_minimization
import numpy as np

'''
Pour lancer ce programme, le sortir du dossier minimizer.
'''

### Paramètres ###

# Pays
country = "France"

# Coefficients
# beta_SEIR, sigma_SEIR, gamma_SEIR = 45.70046793, 3.4581713, 45.00777174
beta_SEIR, sigma_SEIR, gamma_SEIR = 397.86333590847744, 49.17696647366713, 397.3828531005903

print("Coefficients optimaux = ", SEIR_minimization(np.array([beta_SEIR, sigma_SEIR, gamma_SEIR]), country))
