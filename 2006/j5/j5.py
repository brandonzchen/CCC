lista = [[0 for i in range(8)] for j in range(8)]
lista[3][3] = 1
lista[4][4] = 1
lista[3][4] = 2
lista[4][3] = 2

listb = [[0 for i in range(8)] for j in range(8)]
for i in range(8):
    for j in range(8):
        if i == j:
            listb[i][j] = 2
        if i + j == 7:
            listb[i][j] = 1

listc = [[0 for i in range(8)] for j in range(8)]
for i in range(8):
    for j in range(8):
        if j == 2 or j == 3:
            listc[i][j] = 2
        if j ==4 or j ==5:
            listc[i][j] = 1
