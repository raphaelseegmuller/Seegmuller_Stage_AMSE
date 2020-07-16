from libs.useful_fcts import SIR_minimization
import numpy as np

'''
Pour lancer ce programme, le sortir du dossier minimizer.
'''

### Paramètres ###

# Pays
country = "France"

# Coefficients
beta_SIR, gamma_SIR = 43.01327559046377, 42.96070458702876

print("Coefficients optimaux = ", SIR_minimization(np.array([beta_SIR, gamma_SIR]), country))
