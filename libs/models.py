import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize


def euler_explicite1(f, tinit, Tfinal, y0, h):
    N = int((Tfinal - tinit) / h)  # ou floor((Tfinal-tinit)/h)
    Y = np.array([[0, 0, 0]] * (N + 1))  # Tableau numpy avec que des zéros
    t = tinit + h * np.arange(
        N + 1)  # Tableau numpy contenant les entiers de 0 à N, t = (tinit, tinit + h, tinit + 2h, ...)
    Y[0] = y0
    for n in range(N):
        Y[n + 1] = Y[n] + h * f(t[n], Y[n])
    return Y


def f_SIR(F, beta, gamma):
    return np.array([-beta * F[0] * F[1], (beta * F[0] * F[1]) - (gamma * F[1]), gamma * F[1]])


def f_SEIR(F, beta, gamma, sigma):
    return np.array(
        [-beta * F[0] * F[2], (beta * F[0] * F[2]) - (sigma * F[1]), (sigma * F[1]) - (gamma * F[2]), gamma * F[2]])


def logistique(C0, K, r, t):
    C = np.zeros((len(r), len(t)))
    for indice in range(len(r)):
        for d in range(len(t)):
            C[indice][d] = (K * C0) / (C0 + (K - C0) * np.exp(-r[indice] * t[d]))
    return C


def richards(C0, K, r, t, alpha):
    C = np.zeros((len(r), len(t)))
    for indice in range(len(r)):
        for d in range(len(t)):
            C[indice][d] = (K * C0) / (
                    C0 ** alpha + (K ** alpha - C0 ** alpha) * np.exp((-r[indice] * t[d] * (K ** alpha)) / (
                    K ** alpha - C0 ** alpha)) ** (1 / alpha))
    return C


def SIR(beta, gamma, t, start):
    Y = np.array([[0, 0, 0]] * (len(t)))  # Tableau numpy avec que des zéros
    Y[0] = start
    h = t[1] - t[0]
    for n in range(len(t) - 1):
        Y[n + 1] = Y[n] + h * f_SIR(Y[n], beta, gamma)
    return Y


def SEIR(beta, gamma, sigma, t, start):
    Y = np.array([[0, 0, 0, 0]] * (len(t)))  # Tableau numpy avec que des zéros
    Y[0] = start
    h = t[1] - t[0]
    for n in range(len(t) - 1):
        Y[n + 1] = Y[n] + h * f_SEIR(Y[n], beta, gamma, sigma)
    return Y


# def mini(f, reel):
#     return minimize(f, reel)

