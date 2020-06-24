import numpy as np


def error(y_obs, y_pred):
    assert len(y_obs) == len(y_pred)
    res = 0
    for t_value in range(len(y_obs)):
        res += (y_obs[t_value] - y_pred[t_value]) ** 2
    return res


def converter(path):
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

    data_file = open(path, 'r')
    matrix = []
    for line in data_file:
        matrix += [[]]
        comma_counter = 0
        number = ""
        for element in line:
            if comma_counter >= 3:
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
    data_file.close()
    return final_matrix


def get_OxCGRT(matrix):
    C1 = []
    for t in range(len(matrix)):
        if matrix[t][1] == None:
            C1 += [(100 * matrix[t][0]) / 3]
        else:
            C1 += [(100 * matrix[t][0] - 0.5 * (1 - matrix[t][1])) / 3]

    C2 = []
    for t in range(len(matrix)):
        if matrix[t][3] == None:
            C2 += [(100 * matrix[t][2]) / 3]
        else:
            C2 += [(100 * matrix[t][2] - 0.5 * (1 - matrix[t][3])) / 3]

    C3 = []
    for t in range(len(matrix)):
        if matrix[t][5] == None:
            C3 += [(100 * matrix[t][4]) / 2]
        else:
            C3 += [(100 * matrix[t][4] - 0.5 * (1 - matrix[t][5])) / 2]

    C4 = []
    for t in range(len(matrix)):
        if matrix[t][7] == None:
            C4 += [(100 * matrix[t][6]) / 4]
        else:
            C4 += [(100 * matrix[t][6] - 0.5 * (1 - matrix[t][7])) / 4]

    C5 = []
    for t in range(len(matrix)):
        if matrix[t][9] == None:
            C5 += [(100 * matrix[t][8]) / 2]
        else:
            C5 += [(100 * matrix[t][8] - 0.5 * (1 - matrix[t][9])) / 2]

    C6 = []
    for t in range(len(matrix)):
        if matrix[t][11] == None:
            C6 += [(100 * matrix[t][10]) / 3]
        else:
            C6 += [(100 * matrix[t][10] - 0.5 * (1 - matrix[t][11])) / 3]

    C7 = []
    for t in range(len(matrix)):
        if matrix[t][13] == None:
            C7 += [(100 * matrix[t][12]) / 2]
        else:
            C7 += [(100 * matrix[t][12] - 0.5 * (1 - matrix[t][13])) / 2]

    C8 = []
    for t in range(len(matrix)):
        C8 += [(100 * matrix[t][14]) / 4]

    E1 = []
    for t in range(len(matrix)):
        if matrix[t][16] == None:
            E1 += [(100 * matrix[t][15]) / 2]
        else:
            E1 += [(100 * matrix[t][15] - 0.5 * (1 - matrix[t][16])) / 2]

    E2 = []
    for t in range(len(matrix)):
        E2 += [(100 * matrix[t][17]) / 2]

    H1 = []
    for t in range(len(matrix)):
        if matrix[t][21] == None:
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
