from libs.useful_fcts import SIR_minimization
import numpy as np

### Paramètres ###

# Pays
country = "France"

# Coefficients
beta_SIR, gamma_SIR = 10.26658877, 10.1508766

print("Coefficients optimaux = ", SIR_minimization(np.array([beta_SIR, gamma_SIR]), country))
