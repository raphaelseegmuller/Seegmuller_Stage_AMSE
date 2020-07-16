import numpy as np
from sklearn.decomposition import PCA

from libs.useful_fcts import *


# Jean 6 6 5 5,5 8
# Aline 8 8 8 8 9
# Annie 6 7 11 9,5 11
# Monique 14,5 14,5 15,5 15 8
# Didier 14 14 12 12 10
# André 11 10 5,5 7 13
# Pierre 5,5 7 14 11,5 10
# Brigitte 13 12,5 8,5 9,5 12
# Evelyne 9 9,5 12,5 12 18

A = np.array([
    [6, 6, 5, 5.5, 8],
    [8, 8, 8, 8, 9],
    [6, 7, 11, 9.5, 11],
    [14.5, 14.5, 15.5, 15, 8],
    [14, 14, 12, 12, 10],
    [11, 10, 5.5, 7, 13],
    [5.5, 7, 14, 11.5, 10],
    [13, 12.5, 8.5, 9.5, 12],
    [9, 9.5, 12.5, 12, 18]
])

print(reduction(A))
print(process_matrix(A))
print(sort_eigenvalues(process_matrix(A)[0]))

print("#########################")
print(compute_new_data_matrix(A, process_matrix(A)[1], process_matrix(A)[0], 3))

print("SECOND METHODE")

pca = PCA(n_components=3)
pca.fit(A)
print(pca.transform(A))
