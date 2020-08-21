from libs.useful_fcts import *
import numpy as np
from sklearn.metrics import calinski_harabasz_score
import matplotlib.pyplot as plt

country_list = ["Allemagne", "Autriche", "Belgique", "Danemark", "Espagne", "France", "Islande", "Italie", "Pays-Bas",
                "Royaume-Uni", "Suède", "Suisse"]

days_around = 30

cluster_nbr = 7

M = give_list_around_mid_point_2(country_list, days_around)

print("M : ", M)
eig_values, eig_vectors = process_matrix(M)
print("eig_values : ", eig_values)
print("eig_vectors", eig_vectors)
truc = sort_eigenvalues(eig_values)
print("truc : ", truc)
print("##########################################")
new_M = compute_new_data_matrix(M, eig_vectors, eig_values, cluster_nbr)
print("new_M : ", new_M)
labels, inertia = get_DATA_2D_in_clusters(M, cluster_nbr)
print("labels : ", labels.tolist())
print("inertia : ", inertia)
plot_DATA_2D_in_clusters(new_M, labels)

### Détermination du nombre optimal de cluster en utilisant l'indice de Calinski-Harabarasz ###


# prediction = [np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) for i in range(12)]
#
# prediction[0] = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# prediction[1] = np.array([1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0])
# prediction[2] = np.array([2, 0, 2, 0, 2, 2, 0, 0, 0, 1, 1, 0])
# prediction[3] = np.array([2, 0, 2, 0, 2, 2, 0, 0, 0, 1, 3, 0])
# prediction[4] = np.array([2, 0, 2, 0, 2, 2, 4, 0, 0, 1, 3, 0])
# prediction[5] = np.array([2, 0, 5, 0, 2, 2, 4, 0, 0, 1, 3, 0])
# prediction[6] = np.array([2, 0, 5, 0, 2, 2, 4, 6, 0, 1, 3, 0])
# prediction[7] = np.array([2, 0, 6, 0, 5, 5, 1, 7, 0, 3, 4, 0])
# prediction[8] = np.array([2, 0, 6, 8, 5, 5, 1, 7, 0, 3, 4, 0])
# prediction[9] = np.array([2, 0, 6, 8, 5, 9, 1, 7, 0, 3, 4, 0])
# prediction[10] = np.array([2, 10, 6, 8, 5, 9, 1, 7, 0, 3, 4, 0])
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

# inertia_1 = get_DATA_2D_in_clusters(M, 1)[1]
# inertia_2 = get_DATA_2D_in_clusters(M, 2)[1]
# inertia_3 = get_DATA_2D_in_clusters(M, 3)[1]
# inertia_4 = get_DATA_2D_in_clusters(M, 4)[1]
# inertia_5 = get_DATA_2D_in_clusters(M, 5)[1]
# inertia_6 = get_DATA_2D_in_clusters(M, 6)[1]
# inertia_7 = get_DATA_2D_in_clusters(M, 7)[1]
# inertia_8 = get_DATA_2D_in_clusters(M, 8)[1]
# inertia_9 = get_DATA_2D_in_clusters(M, 9)[1]
# inertia_10 = get_DATA_2D_in_clusters(M, 10)[1]
# inertia_11 = get_DATA_2D_in_clusters(M, 11)[1]
# inertia_12 = get_DATA_2D_in_clusters(M, 12)[1]
#
# inertia_list = [inertia_1, inertia_2, inertia_3, inertia_4, inertia_5, inertia_6, inertia_7, inertia_8, inertia_9,
#                 inertia_10, inertia_11, inertia_12]
#
# absc = np.arange(1, 13)
#
# plt.plot(absc, inertia_list)

plt.show()
