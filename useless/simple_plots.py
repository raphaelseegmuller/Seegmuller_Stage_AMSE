import numpy as np
import matplotlib.pyplot as plt
import dash
import dash_core_components as dcc

from libs.models import *
import data as dt


# Défintion des paramètres
C0 = 21
# K = 52128
K = 151753
# taux de croissance exponentielle
# r = np.arange(1, 1.1, 0.01)
r = np.array([1])
t = np.arange(0, 29, 1)
alpha1 = 1
alpha2 = 1.05
alpha3 = 1.1


C1 = logistique(C0, K, r, t)
for i in range(len(C1)):
    plt.plot(t, C1[i])

C2 = richards(C0, K, r, t, alpha1)
for i in range(len(C2)):
    plt.plot(t, C2[i])



# C3 = richards(C0, K, r, t, alpha2)
# for i in range(len(C3)):
#     plt.plot(t, C3[i])
#
# C4 = richards(C0, K, r, t, alpha3)
# for i in range(len(C4)):
#     plt.plot(t, C4[i])

# plt.plot(t, dt.C)

plt.title("Comparaison des modèles phénoménologiques")
plt.legend([r"logistique", r"richards, $\alpha = 1$", r"richards, $\alpha = 1.05$", r"richards, $\alpha = 1.1$"], bbox_to_anchor =(1,-0.2), loc = "upper right")
# plt.legend([r"logistique", r"richards, $\alpha = 1$", r"richards, $\alpha = 1.05$", r"richards, $\alpha = 1.1$", r"réel"], bbox_to_anchor =(1,-0.2), loc = "upper right")
plt.xlabel(r"Temps $t$")
plt.ylabel(r"Nombre de cas total   $C$")
plt.show()
