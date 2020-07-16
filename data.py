import numpy as np

# 22 janvier --> 23 juin
Time = ["22/01", "23/01", "24/01", "25/01", "26/01", "27/01", "28/01", "29/01", "30/01", "31/01", "01/02", "02/02",
        "03/02", "04/02", "05/02", "06/02", "07/02", "08/02", "09/02", "10/02", "11/02", "12/02", "13/02", "14/02",
        "15/02", "16/02", "17/02", "18/02", "19/02", "20/02", "21/02", "22/02", "23/02", "24/02", "25/02", "26/02",
        "27/02", "28/02", "29/02", "01/03", "02/03", "03/03", "04/03", "05/03", "06/03", "07/03", "08/03", "09/03",
        "10/03", "11/03", "12/03", "13/03", "14/03", "15/03", "16/03", "17/03", "18/03", "19/03", "20/03", "21/03",
        "22/03", "23/03", "24/03", "25/03", "26/03", "27/03", "28/03", "29/03", "30/03", "31/03", "01/04", "02/04",
        "03/04", "04/04", "05/04", "06/04", "07/04", "08/04", "09/04", "10/04", "11/04", "12/04", "13/04", "14/04",
        "15/04", "16/04", "17/04", "18/04", "19/04", "20/04", "21/04", "22/04", "23/04", "24/04", "25/04", "26/04",
        "27/04", "28/04", "29/04", "30/04", "01/05", "02/05", "03/05", "04/05", "05/05", "06/05", "07/05", "08/05",
        "09/05", "10/05", "11/05", "12/05", "13/05", "14/05", "15/05", "16/05", "17/05", "18/05", "19/05", "20/05",
        "21/05", "22/05", "23/05", "24/05", "25/05", "26/05", "27/05", "28/05", "29/05", "30/05", "31/05", "01/06",
        "02/06", "03/06", "04/06", "05/06", "06/06", "07/06", "08/06", "09/06", "10/06", "11/06", "12/06", "13/06",
        "14/06", "15/06"]

# 1 janvier --> 23 juin
Time_ext = ["01/01", "02/01", "03/01", "04/01", "05/01", "06/01", "07/01", "08/01", "09/01", "10/01", "11/01", "12/01",
            "13/01", "14/01", "15/01", "16/01", "17/01", "18/01", "19/01", "20/01", "21/01", "22/01", "23/01", "24/01",
            "25/01", "26/01", "27/01", "28/01", "29/01", "30/01", "31/01", "01/02", "02/02", "03/02", "04/02", "05/02",
            "06/02", "07/02", "08/02", "09/02", "10/02", "11/02", "12/02", "13/02", "14/02", "15/02", "16/02", "17/02",
            "18/02", "19/02", "20/02", "21/02", "22/02", "23/02", "24/02", "25/02", "26/02", "27/02", "28/02", "29/02",
            "01/03", "02/03", "03/03", "04/03", "05/03", "06/03", "07/03", "08/03", "09/03", "10/03", "11/03", "12/03",
            "13/03", "14/03", "15/03", "16/03", "17/03", "18/03", "19/03", "20/03", "21/03", "22/03", "23/03", "24/03",
            "25/03", "26/03", "27/03", "28/03", "29/03", "30/03", "31/03", "01/04", "02/04", "03/04", "04/04", "05/04",
            "06/04", "07/04", "08/04", "09/04", "10/04", "11/04", "12/04", "13/04", "14/04", "15/04", "16/04", "17/04",
            "18/04", "19/04", "20/04", "21/04", "22/04", "23/04", "24/04", "25/04", "26/04", "27/04", "28/04", "29/04",
            "30/04", "01/05", "02/05", "03/05", "04/05", "05/05", "06/05", "07/05", "08/05", "09/05", "10/05", "11/05",
            "12/05", "13/05", "14/05", "15/05", "16/05", "17/05", "18/05", "19/05", "20/05", "21/05", "22/05", "23/05",
            "24/05", "25/05", "26/05", "27/05", "28/05", "29/05", "30/05", "31/05", "01/06", "02/06", "03/06", "04/06",
            "05/06", "06/06", "07/06", "08/06", "09/06", "10/06", "11/06", "12/06", "13/06", "14/06", "15/06", "16/06",
            "17/06", "18/06", "19/06", "20/06", "21/06", "22/06", "23/06"]

### Fin des prises de mesures ###

'''
Certains pays manquent de données à la fin de leur fichier texte. Pour éviter de prendre des données vides, on fixe une
limite.
'''

Ending = dict()

Ending['Afghanistan'] = 0
Ending['Afrique du Sud'] = 5
Ending['Albanie'] = 8
Ending['Algérie'] = 1
Ending['Allemagne'] = 10
Ending['Andorre'] = 1
Ending['Angola'] = 19
Ending['Arabie sahoudite'] = 29
Ending['Argentine'] = 15
Ending['Aruba'] = 12
Ending['Australie'] = 1
Ending['Autriche'] = 5
Ending['Azerbaïdjan'] = 8
Ending['Bangladesh'] = 8
Ending['Barbades'] = 5
Ending['Barheïn'] = 0
Ending['Belgique'] = 2
Ending['Belize'] = 13
Ending['Bénin'] = 12
Ending['Bermudes'] = 5
Ending['Bhoutan'] = 8
Ending['Biélorussie'] = 2
Ending['Birmanie'] = 7
Ending['Bolivie'] = 15
Ending['Bosnie-Herzégovine'] = 11
Ending['Botswana'] = 1
Ending['Brésil'] = 2
Ending['Brunei'] = 1
Ending['Bulgarie'] = 21
Ending['Burkina Faso'] = 1
Ending['Burundi'] = 1
Ending['Cambodge'] = 20
Ending['Cameroun'] = 2
Ending['Canada'] = 12
Ending['Cap-Vert'] = 10
Ending['Chili'] = 12
Ending['Chine'] = 5
Ending['Chypre'] = 5
Ending['Colombie'] = 6
Ending['Congo'] = 2
Ending['Corée du Sud'] = 6
Ending['Costa Rica'] = 1
Ending['Côte d\'Ivoire'] = 12
Ending['Croatie'] = (61, 77, 168)  # trou
Ending['Cuba'] = 5
Ending['Danemark'] = 5
Ending['Djibouti'] = 4
Ending['Dominique'] = 5
Ending['Égypte'] = 12
Ending['Émirats arabes unis'] = 8
Ending['Équateur'] = 5
Ending['Érythrée'] = 4
Ending['Espagne'] = 12
Ending['Estonie'] = 12
Ending['Eswatini'] = 7
Ending['États-Unis'] = 9
Ending['Éthiopie'] = 12
Ending['Fidji'] = 1
Ending['Finlande'] = 7
Ending['France'] = 5
Ending['France2'] = 5
Ending['Gabon'] = 5  # Ne marche pas
Ending['Gambie'] = 5  # trou
Ending['Géorgie'] = 8
Ending['Ghana'] = 9
# Ending['Gibraltar'] = TOUT
Ending['Grèce'] = 5
Ending['Groenland'] = 7
Ending['Guam'] = 2
Ending['Guatemala'] = 2
Ending['Guinée'] = 7
Ending['Guyana'] = 9
Ending['Haïti'] = 1
Ending['Honduras'] = 2
Ending['Hong Kong'] = 8
Ending['Hongrie'] = 5
Ending['Îles Salomon'] = 11
Ending['Inde'] = 6
Ending['Indonésie'] = 1
Ending['Irak'] = 6
Ending['Iran'] = 8
Ending['Irlande'] = 8
Ending['Islande'] = 19
Ending['Israël'] = 5  # Ne marche pas
Ending['Italie'] = 8
Ending['Jamaïque'] = 10
Ending['Japon'] = 30
Ending['Jordanie'] = 5
Ending['Kazakhstan'] = 8
Ending['Kenya'] = 1
Ending['Kirghizistan'] = 1
Ending['Kosovo'] = 8
Ending['Koweït'] = 5
Ending['Laos'] = 10
Ending['Lesotho'] = 3
# Ending['Lettonie'] = BEAUCOUP
Ending['Liban'] = 6
Ending['Libéria'] = 5
Ending['Libye'] = 5
Ending['Lituanie'] = 8
Ending['Luxembourg'] = 13
Ending['Macao'] = 8
Ending['Madagascar'] = 16
Ending['Malaisie'] = 9  # trou
Ending['Malawi'] = 12
Ending['Mali'] = 5
Ending['Maroc'] = 11
Ending['Maurice'] = 9
Ending['Mauritanie'] = 1
Ending['Mexique'] = 12
Ending['Moldavie'] = 0
Ending['Mongolie'] = 11
Ending['Mozambique'] = 7
Ending['Namibie'] = 1
Ending['Népal'] = 5
Ending['Nicaragua'] = 8  # trou
Ending['Niger'] = 2
Ending['Nigéria'] = 8
Ending['Norvège'] = 1  # ne marche pas
Ending['Nouvelle-Zélande'] = 5
Ending['Oman'] = 8
Ending['Ouganda'] = 1
Ending['Ouzbékistan'] = 5
Ending['Pakistan'] = 1
Ending['Palestine'] = 5
Ending['Panama'] = 8
Ending['Papouasie-Nouvelle-Guinée'] = 5  # ne marche pas
Ending['Paraguay'] = 12
Ending['Pays-Bas'] = 5
Ending['Pérou'] = 3
Ending['Philippines'] = 8
Ending['Pologne'] = 0
Ending['Porto Rico'] = 6
Ending['Portugal'] = 10
Ending['Qatar'] = 9
Ending['République centrafricaine'] = 1
Ending['République démocratique du Congo'] = 1
Ending['République dominicaine'] = 12
Ending['Roumanie'] = 5
Ending['Royaume-Uni'] = 2
Ending['Russie'] = 5
Ending['Rwanda'] = 0
Ending['Saint-Marin'] = 8
Ending['Salvador'] = 12
Ending['Sénégal'] = 9
Ending['Serbie'] = 5
Ending['Seychelles'] = 12
Ending['Sierra Leone'] = 5
Ending['Singapour'] = 2
Ending['Slovaquie'] = 5
Ending['Slovénie'] = 2
Ending['Somalie'] = 15  # trou
Ending['Soudan'] = 2
Ending['Soudan du Sud'] = 8
Ending['Sri Lanka'] = 2
Ending['Suède'] = 16
Ending['Suisse'] = 2
Ending['Suriname'] = 12
Ending['Syrie'] = 0
Ending['Taiwan'] = 8
Ending['Tajikistan'] = 1
Ending['Tanzanie'] = 5
Ending['Tchad'] = 2
Ending['Tchéquie'] = 3  # ne marche pas
Ending['Thaïlande'] = 10
Ending['Timor oriental'] = 9
Ending['Togo'] = 1
Ending['Trinité-et-Tobago'] = 4
Ending['Tunisie'] = 13
Ending['Turkmenistan'] = 1
Ending['Turquie'] = 7
Ending['Ukraine'] = 5
Ending['Uruguay'] = 8
Ending['Vanuatu'] = 9
Ending['Vénézuela'] = 11
Ending['Viêt Nam'] = 8
Ending['Yémen'] = 5
Ending['Zambie'] = 8
Ending['Zimbabwe'] = 1

# Population totale
Totpop = dict()

Totpop["Albanie"] = 2846000
Totpop["Allemagne"] = 83020000
Totpop["Autriche"] = 8859000
Totpop["Belgique"] = 11460000
Totpop["Danemark"] = 5806000
Totpop["Espagne"] = 46940000
Totpop["France"] = 66990000
Totpop["Irlande"] = 4904000
Totpop["Islande"] = 364134
Totpop["Italie"] = 60360000
Totpop["Pays-Bas"] = 17280000
Totpop["Portugal"] = 10280000
Totpop["Roumanie"] = 19410000
Totpop["Royaume-Uni"] = 66650000
Totpop["Serbie"] = 6982000
Totpop["Suède"] = 10230000
Totpop["Suisse"] = 8570000

# Données de https://github.com/CSSEGISandData/COVID-19
France_C = np.array(
    [0, 0, 2, 3, 3, 3, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12,
     12, 14, 18, 38, 57, 100, 130, 191, 204, 285, 377, 653, 949, 1126, 1209, 1784, 2281, 2281, 3661, 4469, 4499, 6633,
     7652, 9043, 10871, 12612, 14282, 16018, 19856, 22304, 25233, 29155, 32964, 37575, 40174, 44550, 52128, 56989,
     59105, 64338, 68605, 70478, 74390, 78167, 82048, 86334, 90676, 93790, 120633, 124298, 129257, 132473, 144944,
     146923, 146906, 151808, 154188, 156921, 154715, 157026, 158636, 160292, 160847, 164589, 167605, 165093, 165764,
     165764, 166976, 167272, 167886, 168935, 172465, 173040, 174318, 174758, 175027, 175479, 176207, 175981, 176712,
     177319, 177207, 177240, 177554, 178428, 179069, 179306, 179645, 179964, 179859, 180166, 179887, 180044, 183309,
     183816, 185616, 185851, 185952, 184980, 188836, 185986, 186538, 187067, 187360, 187458, 187599, 187996, 188354,
     188918, 189311, 189602, 189670])

Germany_C = np.array(
    [0, 0, 0, 0, 0, 1, 4, 4, 4, 5, 8, 10, 12, 12, 12, 12, 13, 13, 14, 14, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16,
     16, 16, 16, 17, 27, 46, 48, 79, 130, 159, 196, 262, 482, 670, 799, 1040, 1176, 1457, 1908, 2078, 3675, 4585, 5795,
     7272, 9257, 12327, 15320, 19848, 22213, 24873, 29056, 32986, 37323, 43938, 50871, 57695, 62095, 66885, 71808,
     77872, 84794, 91159, 96092, 100123, 103374, 107663, 113296, 118181, 122171, 124908, 127854, 130072, 131359, 134753,
     137698, 141397, 143342, 145184, 147065, 148291, 150648, 153129, 154999, 156513, 157770, 158758, 159912, 161539,
     163009, 164077, 164967, 165664, 166152, 167007, 168162, 169430, 170588, 171324, 171879, 172576, 173171, 174098,
     174478, 175233, 175752, 176369, 176551, 177778, 178473, 179021, 179710, 179986, 180328, 180600, 181200, 181524,
     182196, 182922, 183189, 183410, 183594, 183879, 184121, 184472, 184924, 185450, 185750, 186109, 186506, 186522,
     186691, 187226, 187267, 187518, 187682])
