from libs.useful_fcts import *

country_list = ["Allemagne", "Autriche", "Belgique", "Danemark", "Espagne", "France", "Islande", "Italie", "Pays-Bas",
                "Royaume-Uni", "Suède", "Suisse"]

cluster_nbr = 7

M = select_index(give_list_mid_point(country_list))
print("M : ", M)
eig_values, eig_vectors = process_matrix(M)
print("eig_values : ", eig_values)
print("eig_vectors", eig_vectors)
truc = sort_eigenvalues(eig_values)
print("truc : ", truc)
print("##########################################")
new_M = compute_new_data_matrix(M, eig_vectors, eig_values, cluster_nbr)
print("new_M : ", new_M)
labels, inertia = get_DATA_2D_in_clusters(new_M, cluster_nbr)
print("labels : ", labels)
print("inertia : ", inertia)
plot_DATA_2D_in_clusters(new_M, labels)

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
#
# inertia_list = [inertia_1, inertia_2, inertia_3, inertia_4, inertia_5, inertia_6, inertia_7, inertia_8, inertia_9,
#                 inertia_10, inertia_11, inertia_12]
# absc = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#
# plt.plot(absc, inertia_list)
# plt.xlabel("Nombre de clusters")
# plt.ylabel("Inertie totale")

plt.show()
