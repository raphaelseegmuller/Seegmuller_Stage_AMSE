from libs.useful_fcts import *
import numpy as np
from sklearn.metrics import calinski_harabasz_score
import matplotlib.pyplot as plt

country_list = ["Allemagne", "Autriche", "Belgique", "Danemark", "Espagne", "France", "Islande", "Italie", "Pays-Bas",
                "Royaume-Uni", "Suède", "Suisse"]

days_around = 30

cluster_nbr = 7

flag = False
"""
Le programme ne fonctionne pas avec True comme valeur de flag à cause du manque de valeur dans les données de certains 
pays.
"""

if flag:
    M = give_list_around_mid_point_flag(country_list, days_around)
else:
    M = give_list_around_mid_point(country_list, days_around)

print("M : ", M.tolist())
eig_values, eig_vectors = process_matrix(M)
print("eig_values : ", eig_values)
print("eig_vectors", eig_vectors)
truc = sort_eigenvalues(eig_values)
print("truc : ", truc)
print("##########################################")
new_M = compute_new_data_matrix(M, eig_vectors, eig_values, cluster_nbr)
print("new_M : ", new_M)
labels, inertia = get_DATA_2D_in_clusters(new_M, cluster_nbr)
print("labels : ", labels.tolist())
print("inertia : ", inertia)
plot_DATA_2D_in_clusters(new_M, labels)

### Détermination du nombre optimal de cluster en utilisant l'indice de Calinski-Harabarasz ###

# if flag:
#      prediction = [np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) for i in range(20)]
# else:
#      prediction = [np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) for i in range(12)]
#
# prediction[0] = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# prediction[1] = np.array([0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0])
# prediction[2] = np.array([0, 0, 0, 1, 0, 0, 1, 2, 0, 0, 1, 0])
# prediction[3] = np.array([0, 1, 0, 1, 0, 0, 1, 2, 0, 0, 3, 0])
# prediction[4] = np.array([1, 2, 1, 2, 1, 1, 2, 0, 1, 4, 3, 1])
# prediction[5] = np.array([0, 1, 0, 1, 0, 0, 3, 5, 0, 4, 2, 0])
# prediction[6] = np.array([3, 4, 3, 4, 3, 3, 2, 0, 1, 6, 5, 1])
# prediction[7] = np.array([1, 2, 1, 6, 2, 2, 3, 5, 7, 4, 0, 7])
# prediction[8] = np.array([8, 0, 2, 7, 2, 2, 4, 3, 6, 5, 1, 6])
# prediction[9] = np.array([5, 8, 9, 4, 0, 0, 1, 3, 7, 6, 2, 7])
# prediction[10] = np.array([8, 1, 10, 7, 2, 2, 5, 4, 9, 6, 3, 0])
# prediction[11] = np.array([8, 9, 0, 1, 7, 11, 6, 4, 2, 5, 3, 10])
#
#
# absc1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#
#
# chs_matrix = []
# for cluster_nbr in range(1, len(prediction) - 1):
#      chs_matrix += [calinski_harabasz_score(new_M, prediction[cluster_nbr])]
#
# print(chs_matrix)
# plt.plot(absc1, chs_matrix)

### Détermination du nombre optimal de clusters en utilisant l'inertie ###

# inertia_1 = get_DATA_2D_in_clusters(new_M, 1)[1]
# inertia_2 = get_DATA_2D_in_clusters(new_M, 2)[1]
# inertia_3 = get_DATA_2D_in_clusters(new_M, 3)[1]
# inertia_4 = get_DATA_2D_in_clusters(new_M, 4)[1]
# inertia_5 = get_DATA_2D_in_clusters(new_M, 5)[1]
# inertia_6 = get_DATA_2D_in_clusters(new_M, 6)[1]
# inertia_7 = get_DATA_2D_in_clusters(new_M, 7)[1]
# inertia_8 = get_DATA_2D_in_clusters(new_M, 8)[1]
# inertia_9 = get_DATA_2D_in_clusters(new_M, 9)[1]
# inertia_10 = get_DATA_2D_in_clusters(new_M, 10)[1]
# inertia_11 = get_DATA_2D_in_clusters(new_M, 11)[1]
# inertia_12 = get_DATA_2D_in_clusters(new_M, 12)[1]
# if flag:
#      inertia_13 = get_DATA_2D_in_clusters(new_M, 13)[1]
#      inertia_14 = get_DATA_2D_in_clusters(new_M, 14)[1]
#      inertia_15 = get_DATA_2D_in_clusters(new_M, 15)[1]
#      inertia_16 = get_DATA_2D_in_clusters(new_M, 16)[1]
#      inertia_17 = get_DATA_2D_in_clusters(new_M, 17)[1]
#      inertia_18 = get_DATA_2D_in_clusters(new_M, 18)[1]
#      inertia_19 = get_DATA_2D_in_clusters(new_M, 19)[1]
#      inertia_20 = get_DATA_2D_in_clusters(new_M, 20)[1]
#      inertia_list = [inertia_1, inertia_2, inertia_3, inertia_4, inertia_5, inertia_6, inertia_7, inertia_8, inertia_9,
#                      inertia_10, inertia_11, inertia_12, inertia_13, inertia_14, inertia_15, inertia_16, inertia_17,
#                      inertia_18, inertia_19, inertia_20]
# else:
#      inertia_list = [inertia_1, inertia_2, inertia_3, inertia_4, inertia_5, inertia_6, inertia_7, inertia_8, inertia_9,
#                      inertia_10, inertia_11, inertia_12]
#
# if flag:
#      absc = np.arange(1, 21)
# else:
#      absc = np.arange(1, 13)
#
# plt.plot(absc, inertia_list)

plt.show()
