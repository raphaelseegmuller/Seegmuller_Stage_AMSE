import numpy as np
from plotly.subplots import make_subplots
from scipy.optimize import minimize
import scipy.linalg
from math import ceil
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

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
    :param normalize: str
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
    Obtention de la date de la première augmentation du Government response index ainsi que sa valeur.
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
    Obtention de la date de détection des premiers cas ainsi que de leur nombre.
    :param name_list: list -> Liste de pays
    :return: numpy.ndarray
    """
    matrix = []
    for name in name_list:
        sp = CC_starting_point(name)
        matrix += [[sp, converter("data_text/{}".format(name))[sp][27]]]
    matrix = np.asarray(matrix)
    return matrix


def give_CC_matrix(name):
    """
    Obtention du nombre cumulé de cas de COVID 19 en fonction du temps.
    :param name: str -> Nom du pays
    :return: numpy.ndarray
    """
    data = converter("data_text/{}".format(name))[CC_starting_point(name):]
    matrix = []
    for t in range(len(data)):
        matrix += [data[t][27]]
    matrix = np.asarray(matrix)
    return matrix


def give_listCC_matrix(name_list):
    """
    Obtention du nombre cumulé de cas de COVID 19 en fonction du temps pour une liste de pays.
    :param name_list: list, numpy.ndarray
    :return: numpy.ndarray
    """
    final_matrix = []
    for name in name_list:
        data = converter("data_text/{}".format(name))[CC_starting_point(name):]
        matrix = []
        for t in range(len(data)):
            matrix += [data[t][27]]
        final_matrix += [matrix]
    return np.asarray(final_matrix)


def mid_point(name):
    """
    Obtention de la date du milieu de l'épidémie. La date est obtenue en nomre de jours après le 1er janvier 2020.
    :param name: str -> Nom du pays
    :return: int
    """
    matrix = converter("data_text/{}".format(name))
    starting_point = CC_starting_point(name)
    return ceil((len(matrix) - starting_point) / 2) + starting_point


def give_list_mid_point(name_list):
    """
    Obtention des données de différents pays au milieu de l'épidémie.
    :param name_list: list, numpy.ndarray
    :return: numpy.ndarray
    """
    matrix = []
    for name in name_list:
        matrix += [converter("data_text/{}".format(name))[mid_point(name)]]
    return np.asarray(matrix)


def select_index(matrix_init):
    """
    Obtention des indices utilisés pour réaliser l'ACP.
    :param matrix_init: numpy.ndarray
    :return: numpy.ndarray
    """
    matrix = matrix_init.tolist()
    new_matrix = []
    for country in range(len(matrix)):
        new_matrix += [[matrix[country][0]] + [matrix[country][2]] + [matrix[country][4]] + [matrix[country][6]] + [
            matrix[country][8]] + [matrix[country][10]] + [matrix[country][12]] + matrix[country][14:16] +
                       [matrix[country][17]] + matrix[country][22:24]]
    return np.asarray(new_matrix)


def give_list_around_mid_point(name_list, days_around):
    """
    Obtention des indices utilisés pour réaliser l'ACP autour du point de milieu d'épidémie.
    :param name_list: list, numpy.ndarray
    :param days_around: int
    :return: numpy.ndarray
    """
    matrix = []
    for name in name_list:
        index = []
        md = mid_point(name)
        data = converter("data_text/{}".format(name))
        for date in range(md - days_around, md + days_around + 1):
            index += [data[date][0], data[date][2], data[date][4], data[date][6], data[date][8], data[date][10],
                      data[date][12], data[date][14], data[date][15], data[date][17], data[date][22], data[date][23]]
        matrix += [index]
    return np.asarray(matrix)


def give_list_around_mid_point_flag(name_list, days_around):
    """
    Obtention des indices (avec les valeurs de flag) utilisés pour réaliser l'ACP autour du point de milieu d'épidémie.
    :param name_list: list, numpy.ndarray
    :param days_around: int
    :return: numpy.ndarray
    """
    matrix = []
    for name in name_list:
        index = []
        md = mid_point(name)
        data = converter("data_text/{}".format(name))
        for date in range(md - days_around, md + days_around + 1):
            index += [data[date][0], data[date][1], data[date][2], data[date][3], data[date][4], data[date][5],
                      data[date][6], data[date][7], data[date][8], data[date][9], data[date][10], data[date][11],
                      data[date][12], data[date][13], data[date][14], data[date][15], data[date][16], data[date][17],
                      data[date][22], data[date][23]]
            # Fonction pas applicable à cause du manque de données de flag pour certains pays.
        matrix += [index]
    return np.asarray(matrix)


def give_list_around_mid_point_2(name_list, days_around):
    """
    Obtention des indices utilisés pour réaliser l'ACP autour du point de milieu d'épidémie.
    :param name_list: list, numpy.ndarray
    :param days_around: int
    :return: numpy.ndarray
    """
    matrix = []
    for name in name_list:
        index = []
        md = mid_point(name)
        data = converter("data_text/{}".format(name))
        for date in [md - days_around, md, md + days_around]:
            index += [data[date][0], data[date][2], data[date][4], data[date][6], data[date][8], data[date][10],
                      data[date][12], data[date][14], data[date][15], data[date][17], data[date][22], data[date][23]]
        matrix += [index]
    return np.asarray(matrix)


def give_average_matrix(name_list, days_around):
    """
    Obtention de la moyenne des indices pour une durée de deux semaines autour du temps de milieu d'épidémie.
    :param name_list: list, numpy.ndarray
    :param days_around: int
    :return: numpy.ndarray
    """
    matrix = []
    for num_name in range(len(name_list)):
        matrix += [[]]
        data = converter("data_text/{}".format(name_list[num_name]))
        md = mid_point(name_list[num_name])
        index_list = [0, 2, 4, 6, 8, 10, 12, 14, 15, 17, 22, 23]
        for i in index_list:
            index = []
            for date in range(md - days_around, md + days_around + 1):
                index += [data[date][i]]
            av_index = np.mean(np.asarray(index))
            matrix[num_name] += [av_index]
    return np.asarray(matrix)


def fig_creator_md_inter(name, coeff_list):
    """
    Création de figure pour models_interractive.py : Représentation des différents modèles et de la courbe réelle du
    nombre cumulé de cas de la COVID 19.
    :param name: str -> Nom du pays
    :param coeff_list: list -> Liste des paramètres des différents modèles dans cet ordre : [r_log, r_rich, alpha,
    beta_SIR, gamma_SIR, beta_SEIR, sigma_SEIR, gamma_SEIR]
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
    matrix = give_CC_matrix(name)
    sp = CC_starting_point(name)

    ### Défintion des paramètres ###

    # Nombre initial d'infectés.
    C0 = matrix[0]
    # Nombre cumulatif final d'infectés.
    K = matrix[len(matrix) - 1]
    # Intervalles de temps.
    t = np.arange(sp, len(dt.Time_ext), 1)
    # Population totale.
    N = dt.Totpop[name]
    # Nombre initial d'individus infectés, infectieux et guéris.
    E0, I0, R0 = 0, C0, 0
    # Nombre d'individu susceptibles d'attrapper la maladie.
    S0 = N - E0 - I0 - R0

    # Modèles calculant le nombre cumulé d'infectés.
    C1 = md.logistique(C0, K, coeff_list[0], t)  # modèle logistique
    C2 = md.richards(C0, K, coeff_list[1], t, coeff_list[2])  # modèle de Richards
    C3 = md.SIR(S0, I0, R0, t, N, coeff_list[3], coeff_list[4])  # modèle SIR
    C4 = md.SEIR(S0, E0, I0, R0, t, N, coeff_list[5], coeff_list[6], coeff_list[7])  # modèle SEIR

    ### Ajout des courbes ###

    fig.add_scatter(
        x=dt.Time_ext[sp:],
        y=matrix,
        name=name)

    fig.add_scatter(
        x=dt.Time_ext[sp:],
        y=C1, name="Modèle logistique")

    fig.add_scatter(
        x=dt.Time_ext[sp:],
        y=C2, name="Modèle de Richards")

    fig.add_scatter(
        x=dt.Time_ext[sp:],
        y=C3, name="Modèle SIR")

    fig.add_scatter(
        x=dt.Time_ext[sp:],
        y=C4, name="Modèle SEIR")

    return fig


def fig_creator_CC_comparator(name_list, normalize, normalize2, days_around):
    """
    Création de figure représentant le nombre cumulé d'individus contaminés par la COVID 19 en fonction du temps. Les
    données viennent de 'data_text'.
    :param name_list: list -> Liste de pays
    :param normalize: str
    :param normalize2: str
    :param days_around: int
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
        xaxis={'title': 'Date (nombre de jour du milieu de l\'épidémie)'},
        yaxis={'title': 'Nombre d\'individu'}
    )
    time_list = np.arange(-days_around, days_around + 1, 1)
    for name in name_list:
        md = mid_point(name)
        data = converter("data_text/{}".format(name))[md - days_around:md + days_around + 1]
        matrix = []
        for t in range(len(data)):
            if normalize2 == "Non":
                if normalize == "Non":
                    matrix += [data[t][27]]
                else:  # Normalisation de la courbe entre 0 et 1
                    matrix += [data[t][27] / dt.Totpop[name]]
            else:
                if normalize == "Non":
                    matrix += [data[t][27] - data[days_around][27]]
                else:  # Normalisation de la courbe entre 0 et 1
                    matrix += [(data[t][27] - data[days_around][27]) / dt.Totpop[name]]
        fig.add_scatter(
            x=time_list,
            y=matrix,
            name=name)
    return fig


def fig_creator_C_comparator(name_list, normalize, normalize2, days_around):
    """
    Création de figure représentant le nombre d'individus infectés de la COVID 19 en fonction du temps. Les
    données viennent de 'data_text'.
    :param name_list: list -> Liste de pays
    :param normalize: str
    :param normalize2: str
    :param days_around: int
    :return: plotly.graph_objs._figure.Figure
    """
    fig = make_subplots(rows=1, cols=1)
    title = "Nombre d'infectés - COVID 19"
    fig.update_layout(
        title={
            'text': title,
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        title_font_size=30,
        xaxis={'title': 'Date (nombre de jour du milieu de l\'épidémie)'},
        yaxis={'title': 'Nombre d\'individu'}
    )
    time_list = np.arange(-days_around, days_around + 1, 1)
    for name in name_list:
        md = mid_point(name)
        data = converter("data_text/{}".format(name))[md - days_around:md + days_around + 1]
        matrix = []
        cumulative_number = converter("data_text/{}".format(name))[md - days_around - 1][27]
        for t in range(len(data)):
            if normalize2 == "Non":
                if normalize == "Non":
                    matrix += [data[t][27] - cumulative_number]
                else:  # Normalisation de la courbe entre 0 et 1
                    matrix += [(data[t][27] - cumulative_number) / dt.Totpop[name]]
            else:
                if normalize == "Non":
                    matrix += [data[t][27] - cumulative_number - data[days_around][27] + data[days_around - 1][27]]
                else:  # Normalisation de la courbe entre 0 et 1
                    matrix += [(data[t][27] - cumulative_number - data[days_around][27] + data[days_around - 1][27]) /
                               dt.Totpop[name]]
            cumulative_number = data[t][27]
        fig.add_scatter(
            x=time_list,
            y=matrix,
            name=name)
    return fig


def fig_creator_Cdeath_comparator(name_list, normalize, normalize2, days_around):
    """
    Création de figure représentant le nombre cumulé d'individus décédés de la COVID 19 en fonction du temps. Les
    données viennent de 'data_text'.
    :param name_list: list -> Liste de pays
    :param normalize: str
    :param normalize2: str
    :param days_around: int
    :return: plotly.graph_objs._figure.Figure
    """
    fig = make_subplots(rows=1, cols=1)
    title = "Nombre cumulé de décès - COVID 19"
    fig.update_layout(
        title={
            'text': title,
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        title_font_size=30,
        xaxis={'title': 'Date (nombre de jour du milieu de l\'épidémie)'},
        yaxis={'title': 'Nombre d\'individu'}
    )
    time_list = np.arange(-days_around, days_around + 1, 1)
    for name in name_list:
        md = mid_point(name)
        data = converter("data_text/{}".format(name))[md - days_around:md + days_around + 1]
        matrix = []
        for t in range(len(data)):
            if normalize2 == "Non":
                if normalize == "Non":
                    matrix += [data[t][28]]
                else:  # Normalisation de la courbe entre 0 et 1
                    matrix += [data[t][28] / dt.Totpop[name]]
            else:
                if normalize == "Non":
                    matrix += [data[t][28] - data[days_around][28]]
                else:  # Normalisation de la courbe entre 0 et 1
                    matrix += [(data[t][28] - data[days_around][28]) / dt.Totpop[name]]
        fig.add_scatter(
            x=time_list,
            y=matrix,
            name=name)
    return fig


def fig_creator_death_comparator(name_list, normalize, normalize2, days_around):
    """
    Création de figure représentant le nombre d'individus décédés de la COVID 19 en fonction du temps. Les
    données viennent de 'data_text'.
    :param name_list: list -> Liste de pays
    :param normalize: str
    :param normalize2: str
    :param days_around: int
    :return: plotly.graph_objs._figure.Figure
    """
    fig = make_subplots(rows=1, cols=1)
    title = "Nombre de décès - COVID 19"
    fig.update_layout(
        title={
            'text': title,
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        title_font_size=30,
        xaxis={'title': 'Date (nombre de jour du milieu de l\'épidémie)'},
        yaxis={'title': 'Nombre d\'individu'}
    )
    time_list = np.arange(-days_around, days_around + 1, 1)
    for name in name_list:
        md = mid_point(name)
        data = converter("data_text/{}".format(name))[md - days_around:md + days_around + 1]
        matrix = []
        cumulative_number = converter("data_text/{}".format(name))[md - days_around - 1][28]
        for t in range(len(data)):
            if normalize2 == "Non":
                if normalize == "Non":
                    matrix += [data[t][28] - cumulative_number]
                else:  # Normalisation de la courbe entre 0 et 1
                    matrix += [(data[t][28] - cumulative_number) / dt.Totpop[name]]
            else:
                if normalize == "Non":
                    matrix += [data[t][28] - cumulative_number - data[days_around][28] + data[days_around - 1][28]]
                else:  # Normalisation de la courbe entre 0 et 1
                    matrix += [(data[t][28] - cumulative_number - data[days_around][28] + data[days_around - 1][28]) /
                               dt.Totpop[name]]
            cumulative_number = data[t][28]
        fig.add_scatter(
            x=time_list,
            y=matrix,
            name=name)
    return fig


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

def f_logistic_minimization(coeff, name):
    """
    Obtention d'une valeur représentative de l'erreur entre les observations réelles du nombre cumulé de cas de COVID 19
    et le modèle logistique défini à partir des paramètres de la fonction.
    :param coeff: numpy.ndarray
    :param name: str -> Nom du pays
    :return: float
    """
    sp = int(GRCC_matrix_startCC([name])[0][0])
    C0 = GRCC_matrix_startCC([name])[0][1]
    observations = give_CC_matrix(name)
    K = np.max(observations)
    t = np.arange(sp, len(observations) + sp)
    C = md.logistique(C0, K, coeff, t)
    return error(observations, C)


def logistic_minimization(coeff, name):
    """
    Calcul des coefficients du modèle logistique pour qu'il approche au mieux les données réelles.
    :param coeff: numpy.ndarray
    :param name: str -> Nom du pays
    :return: numpy.ndarray
    """
    return minimize(f_logistic_minimization, coeff, args=(name)).x[0]


# Modèle de Richards #

def f_richards_minimization(coeff, name):
    """
    Obtention d'une valeur représentative de l'erreur entre les observations réelles du nombre cumulé de cas de COVID 19
    et le modèle de Richards défini à partir des paramètres de la fonction.
    :param coeff: numpy.ndarray
    :param name: str -> Nom du pays
    :return: float
    """
    sp = int(GRCC_matrix_startCC([name])[0][0])
    C0 = GRCC_matrix_startCC([name])[0][1]
    observations = give_CC_matrix(name)
    K = np.max(observations)
    t = np.arange(sp, len(observations) + sp)
    C = md.richards(C0, K, coeff[0], t, coeff[1])
    return error(observations, C)


def richards_minimization(coeff, name):
    """
    Calcul des coefficients du modèle de Richards pour qu'il approche au mieux les données réelles.
    :param coeff: numpy.ndarray
    :param name: str -> Nom du pays
    :return: numpy.ndarray
    """
    return minimize(f_richards_minimization, coeff, args=(name)).x


# Modèle SIR #

def f_SIR_minimization(coeff, name):
    """
    Obtention d'une valeur représentative de l'erreur entre les observations réelles du nombre cumulé de cas de COVID 19
    et le modèle SIR défini à partir des paramètres de la fonction.
    :param coeff: numpy.ndarray
    :param name: str -> Nom du pays
    :return: float
    """
    sp = int(GRCC_matrix_startCC([name])[0][0])
    init_I = GRCC_matrix_startCC([name])[0][1]
    observations = give_CC_matrix(name)
    N = dt.Totpop[name]
    t = np.arange(sp, len(observations) + sp)
    C = md.SIR(N - init_I, init_I, 0, t, N, coeff[0], coeff[1])
    return error(observations, C)


def SIR_minimization(coeff, name):
    """
    Calcul des coefficients du modèle SIR pour qu'il approche au mieux les données réelles.
    :param coeff: numpy.ndarray
    :param name: str -> Nom du pays
    :return: numpy.ndarray
    """
    return minimize(f_SIR_minimization, coeff, args=(name)).x


# Modèle SEIR #

def f_SEIR_minimization(coeff, name):
    """
    Obtention d'une valeur représentative de l'erreur entre les observations réelles du nombre cumulé de cas de COVID 19
    et le modèle SEIR défini à partir des paramètres de la fonction.
    :param coeff: numpy.ndarray
    :param name: str -> Nom du pays
    :return: float
    """
    sp = int(GRCC_matrix_startCC([name])[0][0])
    init_I = GRCC_matrix_startCC([name])[0][1]
    observations = give_CC_matrix(name)
    N = dt.Totpop[name]
    t = np.arange(sp, len(observations) + sp)
    C = md.SEIR(N - init_I, 0, init_I, 0, t, N, coeff[0], coeff[1], coeff[2])
    '''
    Le nombre initial de personnes infectées mais pas contagieuses est fixé à 0.
    '''
    return error(observations, C)


def SEIR_minimization(coeff, name):
    """
    Calcul des coefficients du modèle SEIR pour qu'il approche au mieux les données réelles.
    :param coeff: numpy.ndarray
    :param name: str -> Nom du pays
    :return: numpy.ndarray
    """
    return minimize(f_SEIR_minimization, coeff, args=name).x


### Analyse en composantes principales ###


def reduction(matrix):
    """
    Réduction la matrice :
    - Soustraction de chaque colonne à sa moyenne
    - Division de chaque colonne par son écart-type.
    :param matrix: numpy.ndarray
    :return: numpy.ndarray
    """
    new_matrix = np.copy(matrix.T)
    # Soustraction par l'espérance.
    for i in range(new_matrix.shape[0]):
        new_matrix[i] = new_matrix[i] - np.mean(new_matrix[i])
    # Division par l'écart type.
    for i in range(new_matrix.shape[0]):
        std = np.std(new_matrix[i])
        if std != 0:
            new_matrix[i] = new_matrix[i] / std
    return new_matrix.T


def process_matrix(DATA):
    """
    Calcul des valeurs et vecteurs propres correspondant aux composantes principales de DATA.
    :param DATA: numpy.ndarray
    :return: numpy.ndarray
    """
    data_reduced = reduction(DATA)
    corr_matrix = 1 / data_reduced.shape[0] * np.dot(data_reduced.T, data_reduced)
    print("corr_matrix is symetric :", np.all(corr_matrix == corr_matrix.T))
    print("corr_matrix is real :", np.all(corr_matrix == np.real(corr_matrix)))
    val_and_vec = scipy.linalg.eigh(corr_matrix)
    return val_and_vec


def sort_eigenvalues(eigen_values):
    """
    Obtention des valeurs propres triées par ordre décroissant.
    :param eigen_values: numpy.ndarray
    :return: list
    """
    eigen_values = eigen_values.real
    for i in range(len(eigen_values)):
        if np.isclose(0, eigen_values[i]):
            eigen_values[i] = 0
        assert eigen_values[i] >= 0
    p = sum(eigen_values)
    supertuples = [(eigen_values[i], eigen_values[i] / p, i) for i in range(len(eigen_values))]
    supertuples.sort(reverse=True)
    return supertuples


def compute_new_data_matrix(DATA, eig_vectors, eig_values, n):
    """
    Calcul de la nouvelle matrice de données évaluant chaque individu selon les nouvelles variables. Si
    n < len(eig_values), la nouvelle matrice comporte uniquement les n variables les plus dispersives.
    :param DATA: numpy.ndarray -> Matrice de données initiale
    :param eig_vectors: numpy.ndarray
    :param eig_values: numpy.ndarray
    :param n: int
    :return: numpy.ndarray
    """
    assert n <= len(eig_values)

    eig_values = sort_eigenvalues(eig_values)
    eig_values = eig_values[:n]

    new_DATA = np.dot(reduction(DATA), eig_vectors)
    indexes = []
    for v in eig_values:
        indexes.append(v[2])
    new_DATA = new_DATA[:, indexes]
    return new_DATA


def find_clusters(new_DATA, nb_clusters):
    """
    Application du kmean clustering pour trouver les clusters.
    :param new_DATA: numpy.ndarray
    :param nb_clusters: int
    :return: tuple
    """
    kmeans = KMeans(n_clusters=nb_clusters, n_init=12).fit(new_DATA)
    labels = kmeans.labels_
    inertia = kmeans.inertia_
    return labels, inertia


def get_DATA_2D_in_clusters(DATA, nb_clusters):
    """
    Obtention de la projection des individus dans l'espace des 3 variables d'inertie maximale avec clustering.
    :param DATA: numpy.ndarray
    :param nb_clusters: int
    :return: tuple
    """
    if nb_clusters > len(DATA):
        print("Not enough markers to distinguish all the clusters.")
    labels, inertia = find_clusters(DATA, nb_clusters)
    print("Inertia :", inertia)
    return labels, inertia


def plot_DATA_2D_in_clusters(DATA, labels):
    """
    Affichage des individus dans l'espace défini par les deux vecteurs propres représentant les variables les plus
    dispersives.
    :param DATA: numpy.ndarray
    :param labels: numpy.ndarray
    :return: NoneType -> figure matplotlib.pyplot
    """
    K = np.max(labels)
    markerslist = [r"$\mathcal{A}$", r"$\mathcal{B}$", r"$\mathcal{C}$", r"$\mathcal{D}$",
                   r"$\mathcal{E}$", r"$\mathcal{F}$", r"$\mathcal{G}$", r"$\mathcal{H}$", r"$\mathcal{I}$",
                   r"$\mathcal{J}$", r"$\mathcal{K}$", r"$\mathcal{L}$", r"$\mathcal{M}$", r"$\mathcal{N}$",
                   r"$\mathcal{O}$", r"$\mathcal{P}$", r"$\mathcal{Q}$", r"$\mathcal{R}$", r"$\mathcal{S}$",
                   r"$\mathcal{T}$", r"$\mathcal{U}$", r"$\mathcal{V}$", r"$\mathcal{W}$", r"$\mathcal{X}$",
                   r"$\mathcal{Y}$", r"$\mathcal{Z}$"]
    cols = ["blue", "orange", "green", "red", "purple", "grey", "brown", "pink", "purple", "cyan", "beige", "deeppink"]

    for k in range(K + 1):
        l_x = []
        l_y = []
        for i, label in enumerate(labels):
            if label == k:
                indiv = DATA[i]
                x1 = indiv[0]
                y1 = indiv[1]
                l_x.append(x1)
                l_y.append(y1)

        plt.scatter(l_x, l_y, cmap="viridis", marker=markerslist[k], label="Group " + markerslist[k],
                    color=cols[k])  # ,edgecolor='black', linewidth='3')

    plt.gca().set_xlabel(r"Projection sur $X'_1$ (en unité de $\sigma'_1$)")
    plt.gca().set_ylabel(r"Projection sur $X'_2$ (en unité de $\sigma'_2$)")
    plt.legend()
