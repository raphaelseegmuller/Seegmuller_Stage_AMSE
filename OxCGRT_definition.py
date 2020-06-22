import data as dt
import numpy as np

France_C1 = []
for t in range(len(dt.France_OxCGRT)):
    if dt.France_OxCGRT[t][1] == None:
        France_C1 += [(100 * dt.France_OxCGRT[t][0]) / 3]
    else:
        France_C1 += [(100 * dt.France_OxCGRT[t][0] - 0.5 * (1 - dt.France_OxCGRT[t][1])) / 3]

France_C2 = []
for t in range(len(dt.France_OxCGRT)):
    if dt.France_OxCGRT[t][3] == None:
        France_C2 += [(100 * dt.France_OxCGRT[t][2]) / 3]
    else:
        France_C2 += [(100 * dt.France_OxCGRT[t][2] - 0.5 * (1 - dt.France_OxCGRT[t][3])) / 3]

France_C3 = []
for t in range(len(dt.France_OxCGRT)):
    if dt.France_OxCGRT[t][5] == None:
        France_C3 += [(100 * dt.France_OxCGRT[t][4]) / 2]
    else:
        France_C3 += [(100 * dt.France_OxCGRT[t][4] - 0.5 * (1 - dt.France_OxCGRT[t][5])) / 2]

France_C4 = []
for t in range(len(dt.France_OxCGRT)):
    if dt.France_OxCGRT[t][7] == None:
        France_C4 += [(100 * dt.France_OxCGRT[t][6]) / 4]
    else:
        France_C4 += [(100 * dt.France_OxCGRT[t][6] - 0.5 * (1 - dt.France_OxCGRT[t][7])) / 4]

France_C5 = []
for t in range(len(dt.France_OxCGRT)):
    if dt.France_OxCGRT[t][9] == None:
        France_C5 += [(100 * dt.France_OxCGRT[t][8]) / 2]
    else:
        France_C5 += [(100 * dt.France_OxCGRT[t][8] - 0.5 * (1 - dt.France_OxCGRT[t][9])) / 2]

France_C6 = []
for t in range(len(dt.France_OxCGRT)):
    if dt.France_OxCGRT[t][11] == None:
        France_C6 += [(100 * dt.France_OxCGRT[t][10]) / 3]
    else:
        France_C6 += [(100 * dt.France_OxCGRT[t][10] - 0.5 * (1 - dt.France_OxCGRT[t][11])) / 3]

France_C7 = []
for t in range(len(dt.France_OxCGRT)):
    if dt.France_OxCGRT[t][13] == None:
        France_C7 += [(100 * dt.France_OxCGRT[t][12]) / 2]
    else:
        France_C7 += [(100 * dt.France_OxCGRT[t][12] - 0.5 * (1 - dt.France_OxCGRT[t][13])) / 2]

France_C8 = []
for t in range(len(dt.France_OxCGRT)):
    France_C8 += [(100 * dt.France_OxCGRT[t][14]) / 4]

France_E1 = []
for t in range(len(dt.France_OxCGRT)):
    if dt.France_OxCGRT[t][16] == None:
        France_E1 += [(100 * dt.France_OxCGRT[t][15]) / 2]
    else:
        France_E1 += [(100 * dt.France_OxCGRT[t][15] - 0.5 * (1 - dt.France_OxCGRT[t][16])) / 2]

France_E2 = []
for t in range(len(dt.France_OxCGRT)):
    France_E2 += [(100 * dt.France_OxCGRT[t][17]) / 2]

France_H1 = []
for t in range(len(dt.France_OxCGRT)):
    if dt.France_OxCGRT[t][21] == None:
        France_H1 += [(100 * dt.France_OxCGRT[t][20]) / 2]
    else:
        France_H1 += [(100 * dt.France_OxCGRT[t][20] - 0.5 * (1 - dt.France_OxCGRT[t][21])) / 2]

France_H2 = []
for t in range(len(dt.France_OxCGRT)):
    France_H2 += [(100 * dt.France_OxCGRT[t][22]) / 3]

France_H3 = []
for t in range(len(dt.France_OxCGRT)):
    France_H3 += [(100 * dt.France_OxCGRT[t][23]) / 2]

# Government response index
France_GR = []
for t in range(len(dt.France_OxCGRT)):
    France_GR += [np.mean(np.array([France_C1[t], France_C2[t], France_C3[t], France_C4[t], France_C5[t], France_C6[t],
                                    France_C7[t], France_C8[t], France_E1[t], France_E2[t], France_H1[t], France_H2[t],
                                    France_H3[t]]))]

# Containment and health index
France_CH = []
for t in range(len(dt.France_OxCGRT)):
    France_CH += [np.mean(np.array([France_C1[t], France_C2[t], France_C3[t], France_C4[t], France_C5[t], France_C6[t],
                                    France_C7[t], France_C8[t], France_H1[t], France_H2[t], France_H3[t]]))]

# Stringency index
France_S = []
for t in range(len(dt.France_OxCGRT)):
    France_S += [np.mean(np.array([France_C1[t], France_C2[t], France_C3[t], France_C4[t], France_C5[t], France_C6[t],
                                   France_C7[t], France_C8[t], France_H1[t]]))]

# Economic support index
France_ES = []
for t in range(len(dt.France_OxCGRT)):
    France_ES += [np.mean(np.array([France_E1[t], France_E2[t]]))]
