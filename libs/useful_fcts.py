import numpy as np
from plotly.subplots import make_subplots
from scipy.optimize import minimize

import libs.models as md
import data as dt


def converter(path):
    """
    Convertion des données fichiers textes de 'data_text' en matrices numpy. Les lignes correspondent au temps et les
    colonnes aux différents indicateurs énumérés ci-dessous.
    :param path: str -> Nom du fichier texte
    :return: numpy.ndarray
    """

    '''
    "Variation in government responses to COVID-19" data

    C1_School closing,C1_Flag,C2_Workplace closing,C2_Flag,C3_Cancel public events,C3_Flag,C4_Restrictions on gatherings,
    C4_Flag,C5_Close public transport,C5_Flag,C6_Stay at home requirements,C6_Flag,C7_Restrictions on internal movement,
    C7_Flag,C8_International travel controls,E1_Income support,E1_Flag,E2_Debt/contract relief,E3_Fiscal measures,
    E4_International support,H1_Public information campaigns,H1_Flag,H2_Testing policy,H3_Contact tracing,
    H4_Emergency investment in healthcare,H5_Investment in vaccines,M1_Wildcard,ConfirmedCases,ConfirmedDeaths,
    StringencyIndex,StringencyIndexForDisplay,StringencyLegacyIndex,StringencyLegacyIndexForDisplay,
    GovernmentResponseIndex,GovernmentResponseIndexForDisplay,ContainmentHealthIndex,ContainmentHealthIndexForDisplay,
    EconomicSupportIndex,EconomicSupportIndexForDisplay
    '''

    data_file = open(path, 'r')  # Ouverture du fichier
    # Construction de la matrice
    matrix = []
    for line in data_file:
        matrix += [[]]
        comma_counter = 0
        number = ""
        # Extraction des données entre chaque virgule
        for element in line:
            if comma_counter >= 3:  # Les données voulues sont situées après la troisième virgule des lignes
                if element != ",":
                    number += element
            if element == ",":
                if comma_counter >= 3:
                    if number == "":
                        matrix[-1] += [None]
                    else:
                        matrix[-1] += [float(number)]
                number = ""
                comma_counter += 1
    final_matrix = np.asarray(matrix)
    data_file.close()  # Fermeture du fichier
    return final_matrix


def get_OxCGRT(matrix):
    """
    Calcul des indices décrits dans "Variation in government responses to COVID-19" (Hale et al. 2020).
    :param matrix: numpy.ndarray
    :return: tuple
    """
    C1 = []
    for t in range(len(matrix)):
        if matrix[t][1] == None:  # Valeur de flag
            C1 += [(100 * matrix[t][0]) / 3]
        else:
            C1 += [(100 * matrix[t][0] - 0.5 * (1 - matrix[t][1])) / 3]

    C2 = []
    for t in range(len(matrix)):
        if matrix[t][3] == None:  # Valeur de flag
            C2 += [(100 * matrix[t][2]) / 3]
        else:
            C2 += [(100 * matrix[t][2] - 0.5 * (1 - matrix[t][3])) / 3]

    C3 = []
    for t in range(len(matrix)):
        if matrix[t][5] == None:  # Valeur de flag
            C3 += [(100 * matrix[t][4]) / 2]
        else:
            C3 += [(100 * matrix[t][4] - 0.5 * (1 - matrix[t][5])) / 2]

    C4 = []
    for t in range(len(matrix)):
        if matrix[t][7] == None:  # Valeur de flag
            C4 += [(100 * matrix[t][6]) / 4]
        else:
            C4 += [(100 * matrix[t][6] - 0.5 * (1 - matrix[t][7])) / 4]

    C5 = []
    for t in range(len(matrix)):
        if matrix[t][9] == None:  # Valeur de flag
            C5 += [(100 * matrix[t][8]) / 2]
        else:
            C5 += [(100 * matrix[t][8] - 0.5 * (1 - matrix[t][9])) / 2]

    C6 = []
    for t in range(len(matrix)):
        if matrix[t][11] == None:  # Valeur de flag
            C6 += [(100 * matrix[t][10]) / 3]
        else:
            C6 += [(100 * matrix[t][10] - 0.5 * (1 - matrix[t][11])) / 3]

    C7 = []
    for t in range(len(matrix)):
        if matrix[t][13] == None:  # Valeur de flag
            C7 += [(100 * matrix[t][12]) / 2]
        else:
            C7 += [(100 * matrix[t][12] - 0.5 * (1 - matrix[t][13])) / 2]

    C8 = []
    for t in range(len(matrix)):
        C8 += [(100 * matrix[t][14]) / 4]

    E1 = []
    for t in range(len(matrix)):
        if matrix[t][16] == None:  # Valeur de flag
            E1 += [(100 * matrix[t][15]) / 2]
        else:
            E1 += [(100 * matrix[t][15] - 0.5 * (1 - matrix[t][16])) / 2]

    E2 = []
    for t in range(len(matrix)):
        E2 += [(100 * matrix[t][17]) / 2]

    H1 = []
    for t in range(len(matrix)):
        if matrix[t][21] == None:  # Valeur de flag
            H1 += [(100 * matrix[t][20]) / 2]
        else:
            H1 += [(100 * matrix[t][20] - 0.5 * (1 - matrix[t][21])) / 2]

    H2 = []
    for t in range(len(matrix)):
        H2 += [(100 * matrix[t][22]) / 3]

    H3 = []
    for t in range(len(matrix)):
        H3 += [(100 * matrix[t][23]) / 2]

    # Government response index
    GR = []
    for t in range(len(matrix)):
        GR += [np.mean(
            np.array([C1[t], C2[t], C3[t], C4[t], C5[t], C6[t], C7[t], C8[t], E1[t], E2[t], H1[t], H2[t], H3[t]]))]

    # Containment and health index
    CH = []
    for t in range(len(matrix)):
        CH += [np.mean(np.array([C1[t], C2[t], C3[t], C4[t], C5[t], C6[t], C7[t], C8[t], H1[t], H2[t], H3[t]]))]

    # Stringency index
    S = []
    for t in range(len(matrix)):
        S += [np.mean(np.array([C1[t], C2[t], C3[t], C4[t], C5[t], C6[t], C7[t], C8[t], H1[t]]))]

    # Economic support index
    ES = []
    for t in range(len(matrix)):
        ES += [np.mean(np.array([E1[t], E2[t]]))]

    return GR, CH, S, ES


def give_matrix(name):
    """
    Obtention des indices de la fonction get_OxCGRT à partir du nom du pays.
    :param name: str -> Nom du pays
    :return: list
    """
    limit = dt.Ending[name]  # Limite fixée dans 'data.py' (voir pour plus d'explications).
    if limit == 0:
        return [get_OxCGRT(converter("data_text/{}".format(name)))[0],
                get_OxCGRT(converter("data_text/{}".format(name)))[1],
                get_OxCGRT(converter("data_text/{}".format(name)))[2],
                get_OxCGRT(converter("data_text/{}".format(name)))[3]]
    else:
        return [get_OxCGRT(converter("data_text/{}".format(name))[: -limit])[0],
                get_OxCGRT(converter("data_text/{}".format(name))[: -limit])[1],
                get_OxCGRT(converter("data_text/{}".format(name))[: -limit])[2],
                get_OxCGRT(converter("data_text/{}".format(name))[: -limit])[3]]


def fig_creator(name_list, curve):
    """
    Création de figure représentant les indices de la fonction get_OxCGRT pour une liste de pays choisis.
    :param name_list: list -> Liste de pays
    :param curve: list -> Liste des courbes
    :return: plotly.graph_objs._figure.Figure
    """
    fig = make_subplots(rows=1, cols=1)
    title = "OxCGRT - COVID 19"
    fig.update_layout(
        title={
            'text': title,
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        title_font_size=30,
        xaxis={'title': 'Date (jour/mois)'},
        yaxis={'title': 'Valeur de l\'index (sans unité)'}
    )
    for name in name_list:
        matrix = give_matrix(name)
        if 'GR' in curve:
            fig.add_scatter(
                x=dt.Time_ext,
                y=matrix[0],
                name="{} - Government response index".format(name))

        if 'CH' in curve:
            fig.add_scatter(
                x=dt.Time_ext,
                y=matrix[1],
                name="{} - Containment and health index".format(name))

        if 'S' in curve:
            fig.add_scatter(
                x=dt.Time_ext,
                y=matrix[2],
                name="{} - Stringency index".format(name))

        if 'ES' in curve:
            fig.add_scatter(
                x=dt.Time_ext,
                y=matrix[3],
                name="{} - Economic support index".format(name))
    return fig


def fig_creator_CC(name_list, normalize):
    """
    Création de figure représentant le nombre cumulé d'individus contaminés par la COVID 19 en fonction du temps. Les
    données viennent de 'data_text'.
    :param name_list: list -> Liste de pays
    :param normalize: bool
    :return: plotly.graph_objs._figure.Figure
    """
    fig = make_subplots(rows=1, cols=1)
    title = "Nombre cumulé d'infectés - COVID 19"
    fig.update_layout(
        title={
            'text': title,
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        title_font_size=30,
        xaxis={'title': 'Date (jour/mois)'},
        yaxis={'title': 'Nombre d\'individu'}
    )
    for name in name_list:
        limit = dt.Ending[name]  # Limite fixée dans 'data.py' (voir pour plus d'explications).
        if limit == 0:
            data = converter("data_text/{}".format(name))
        else:
            data = converter("data_text/{}".format(name))[:-limit]
        matrix = []
        for t in range(len(data)):
            if normalize == "Non":
                matrix += [data[t][27]]
            else:  # Normalisation de la courbe entre 0 et 1
                matrix += [data[t][27] / dt.Totpop[name]]
        fig.add_scatter(
            x=dt.Time_ext[:-limit],
            y=matrix,
            name=name)
    return fig


def GR_starting_point(name):
    """
    Obtention de la date de la première augmentation du Gouvernement response index. La date est obtenue en nombre de
    jours après le 1er janvier 2020.
    :param name: str -> Nom du pays
    :return: int
    """
    matrix = give_matrix(name)[0]
    starting_point = 0
    for i in range(len(matrix)):
        if matrix[i] != 0:
            starting_point = i
            break
    assert (starting_point != 0)
    return starting_point


def GRCC_matrix_startGR(name_list):
    """
    Obtention de la liste du nombre cumulé de cas de COVID 19 tronquée à partir de la première augmentation du
    Gouvernement response index.
    :param name_list: list -> Liste de pays
    :return: numpy.ndarray
    """
    matrix = []
    for name in name_list:
        sp = GR_starting_point(name)
        matrix += [[sp, converter("data_text/{}".format(name))[sp][27]]]
    matrix = np.asarray(matrix)
    return matrix


def CC_starting_point(name):
    """
    Obtention de la date de la détection du premier cas de COVID 19. La date est obtenue en nombre de jours après le 1er
    janvier 2020.
    :param name: str -> Nom du pays
    :return: int
    """
    matrix = converter("data_text/{}".format(name))
    starting_point = 0
    for i in range(len(matrix)):
        if matrix[i][27] != 0:
            starting_point = i
            break
    assert (starting_point != 0)
    return starting_point


def GRCC_matrix_startCC(name_list):
    """
    Obtention de la liste du nombre cumulé de cas de COVID 19 tronquée à partir de la détection du premier cas de COVID
    19.
    :param name_list: list -> Liste de pays
    :return: numpy.ndarray
    """
    matrix = []
    for name in name_list:
        sp = CC_starting_point(name)
        matrix += [[sp, converter("data_text/{}".format(name))[sp][27]]]
    matrix = np.asarray(matrix)
    return matrix


### Minimisation ###


def error(y_obs, y_pred):
    """
    Calcul d'erreur entre deux listes.
    :param y_obs: list, numpy.ndarray
    :param y_pred: numpy.ndarray
    :return: float
    """
    assert len(y_obs) == len(y_pred)
    res = 0
    for t_value in range(len(y_obs)):
        res += (y_obs[t_value] - y_pred[t_value]) ** 2
    return res


# Modèle logistique #

def f_logistic_minimization(coeff, observations, C0, K):
    """
    Obtention d'une valeur représentative de l'erreur entre les observations réelles du nombre cumulé de cas de COVID 19
    et le modèle logistique défini à partir des paramètres de la fonction.
    :param coeff: numpy.ndarray
    :param observations: list, numpy.ndarray -> Observations réelles
    :param C0: int
    :param K: int
    :return: numpy.ndarray
    """
    t = np.arange(2, len(observations) + 2)
    C = md.logistique(C0, K, coeff, t)
    return error(observations, C)


def logistic_minimization(coeff, others):
    """
    Calcul des coefficients du modèle logistique pour qu'il approche au mieux les données réelles.
    :param coeff: numpy.ndarray
    :param others: tuple
    :return: numpy.ndarray
    """
    return minimize(f_logistic_minimization, coeff, args=others).x


# Modèle de Richards #

def f_richards_minimization(coeff, observations, C0, K):
    """
    Obtention d'une valeur représentative de l'erreur entre les observations réelles du nombre cumulé de cas de COVID 19
    et le modèle de Richards défini à partir des paramètres de la fonction.
    :param coeff: numpy.ndarray
    :param observations: list, numpy.ndarray -> Observations réelles
    :param C0: int
    :param K: int
    :return: numpy.ndarray
    """
    t = np.arange(2, len(observations) + 2)
    C = md.richards(C0, K, coeff[0], t, coeff[1])
    return error(observations, C)


def richards_minimization(coeff, others):
    """
    Calcul des coefficients du modèle de Richards pour qu'il approche au mieux les données réelles.
    :param coeff: numpy.ndarray
    :param others: tuple
    :return: numpy.ndarray
    """
    return minimize(f_richards_minimization, coeff, args=others).x


# Modèle SIR #

def f_SIR_minimization(coeff, observations, init_cond, N):
    """
    Obtention d'une valeur représentative de l'erreur entre les observations réelles du nombre cumulé de cas de COVID 19
    et le modèle SIR défini à partir des paramètres de la fonction.
    :param coeff: numpy.ndarray
    :param observations: list, numpy.ndarray -> Observations réelles
    :param init_cond: tuple
    :param N: int
    :return: numpy.ndarray
    """
    t = np.arange(2, len(observations) + 2)
    C = md.SIR(init_cond[0], init_cond[1], init_cond[2], t, N, coeff[0], coeff[1])
    return error(observations, C)


def SIR_minimization(coeff, others):
    """
    Calcul des coefficients du modèle SIR pour qu'il approche au mieux les données réelles.
    :param coeff: numpy.ndarray
    :param others: tuple
    :return: numpy.ndarray
    """
    return minimize(f_SIR_minimization, coeff, args=others).x


# Modèle SEIR #

def f_SEIR_minimization(coeff, observations, init_cond, N):
    """
    Obtention d'une valeur représentative de l'erreur entre les observations réelles du nombre cumulé de cas de COVID 19
    et le modèle SEIR défini à partir des paramètres de la fonction.
    :param coeff: numpy.ndarray
    :param observations: list, numpy.ndarray -> Observations réelles
    :param init_cond: tuple
    :param N: int
    :return: numpy.ndarray
    """
    t = np.arange(2, len(observations) + 2)
    C = md.SEIR(init_cond[0], init_cond[1], init_cond[2], init_cond[3], t, N, coeff[0], coeff[1], coeff[2])
    return error(observations, C)


def SEIR_minimization(coeff, others):
    """
    Calcul des coefficients du modèle SEIR pour qu'il approche au mieux les données réelles.
    :param coeff: numpy.ndarray
    :param others: tuple
    :return: numpy.ndarray
    """
    return minimize(f_SEIR_minimization, coeff, args=others).x
