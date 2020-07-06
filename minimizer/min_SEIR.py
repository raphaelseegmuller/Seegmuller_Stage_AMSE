from libs.useful_fcts import SEIR_minimization
import numpy as np

### Paramètres ###

# Pays
country = "France"

# Coefficients
beta_SEIR, sigma_SEIR, gamma_SEIR = 43.67699061, 3.51088774, 41.67800878

print("Coefficients optimaux = ", SEIR_minimization(np.array([beta_SEIR, sigma_SEIR, gamma_SEIR]), country))
