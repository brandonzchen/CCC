import sys

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


#2 is black, 1 is white, 0 is no piece
# xpos 4
# ypos 5
#inputx 5
#inputy 6

def getmoves(xpos, ypos, usedlist, blackwhite):
    if blackwhite % 2 == 0:
        for i in range(len(usedlist)):
            for j in range(len(usedlist[i])):
                if i == xpos:
                    if j == ypos:
                        usedlist[i][j] = 2
        #usedlist[i][j]
        flipcount = 0
        for h in range(1, xpos):
            if usedlist[xpos - h][ypos] == 0:
                break
            if usedlist[xpos - h][ypos] == 1:
                flipcount += 1
            if usedlist[xpos - h][ypos] == 2:
                for k in range(1, flipcount + 1):
                    usedlist[xpos - k][ypos] = 2
        flipcount = 0
        for h in range(1, len(usedlist) - (xpos + 1)):
            if usedlist[xpos + h][ypos] == 0:
                break
            if usedlist[xpos + h][ypos] == 1:
                flipcount += 1
            if usedlist[xpos + h][ypos] == 2:
                for k in range(1, flipcount + 1):
                    usedlist[xpos + k][ypos] = 2
        flipcount = 0
        for h in range(1, ypos):
            if usedlist[xpos][ypos - h] == 0:
                break
            if usedlist[xpos][ypos - h] == 1:
                flipcount += 1
            if usedlist[xpos][ypos - h] == 2:
                for k in range(1, flipcount + 1):
                    usedlist[xpos][ypos - k] = 2
        flipcount = 0
        for h in range(1, len(usedlist[xpos]) - (ypos + 1)):
            if usedlist[xpos][ypos + h] == 0:
                break
            if usedlist[xpos][ypos + h] == 1:
                flipcount += 1
            if usedlist[xpos][ypos + h] == 2:
                for k in range(1, flipcount + 1):
                    usedlist[xpos][ypos + k] = 2
        if (len(usedlist) - (xpos + 1)) <= (len(usedlist[xpos]) - (ypos + 1)):
            templimits = (len(usedlist) - (xpos + 1))
        else:
            templimits = (len(usedlist[xpos]) - (ypos + 1))
        flipcount = 0
        for h in range(1, templimits):
            if usedlist[xpos + h][ypos + h] == 0:
                break
            if usedlist[xpos + h][ypos + h] == 1:
                flipcount += 1
            if usedlist[xpos + h][ypos + h] == 2:
                for k in range(1, flipcount + 1):
                    usedlist[xpos + k][ypos + k] = 2
        if xpos + 1 <= (len(usedlist[xpos]) - (ypos + 1)):
            templimits = xpos + 1
        else:
            templimits = (len(usedlist[xpos]) - (ypos + 1))
        flipcount = 0
        for h in range(1, templimits):
            if usedlist[xpos - h][ypos + h] == 0:
                break
            if usedlist[xpos - h][ypos + h] == 1:
                flipcount += 1
            if usedlist[xpos - h][ypos + h] == 2:
                for k in range(1, flipcount + 1):
                    usedlist[xpos - k][ypos + k] = 2
        if xpos + 1 <= ypos + 1:
            templimits = xpos + 1
        else:
            templimits = ypos + 1
        flipcount = 0
        for h in range(1, templimits):
            if usedlist[xpos - h][ypos - h] == 0:
                break
            if usedlist[xpos - h][ypos - h] == 1:
                flipcount += 1
            if usedlist[xpos - h][ypos - h] == 2:
                for k in range(1, flipcount + 1):
                    usedlist[xpos - k][ypos - k] = 2
        if (len(usedlist) - (xpos + 1)) <= ypos + 1:
            templimits = (len(usedlist) - (xpos + 1))
        else:
            templimits = ypos + 1
        flipcount = 0
        for h in range(1, templimits):
            if usedlist[xpos + h][ypos - h] == 0:
                break
            if usedlist[xpos + h][ypos - h] == 1:
                flipcount += 1
            if usedlist[xpos + h][ypos - h] == 2:
                for k in range(1, flipcount + 1):
                    usedlist[xpos + k][ypos - k] = 2
    if blackwhite % 2 != 0:
        for i in range(len(usedlist)):
            for j in range(len(usedlist[i])):
                if i == xpos:
                    if j == ypos:
                        usedlist[i][j] = 1
        flipcount = 0
        for h in range(1, xpos):
            if usedlist[xpos - h][ypos] == 0:
                break
            if usedlist[xpos - h][ypos] == 2:
                flipcount += 1
            if usedlist[xpos - h][ypos] == 1:
                for k in range(1, flipcount + 1):
                    usedlist[xpos - k][ypos] = 1
        flipcount = 0
        for h in range(1, len(usedlist) - (xpos + 1)):
            if usedlist[xpos + h][ypos] == 0:
                break
            if usedlist[xpos + h][ypos] == 2:
                flipcount += 1
            if usedlist[xpos + h][ypos] == 1:
                for k in range(1, flipcount + 1):
                    usedlist[xpos + k][ypos] = 1
        flipcount = 0
        for h in range(1, ypos):
            if usedlist[xpos][ypos - h] == 0:
                break
            if usedlist[xpos][ypos - h] == 2:
                flipcount += 1
            if usedlist[xpos][ypos - h] == 1:
                for k in range(1, flipcount + 1):
                    usedlist[xpos][ypos - k] = 1
        flipcount = 0
        for h in range(1, len(usedlist[xpos]) - (ypos + 1)):
            if usedlist[xpos][ypos + h] == 0:
                break
            if usedlist[xpos][ypos + h] == 2:
                flipcount += 1
            if usedlist[xpos][ypos + h] == 1:
                for k in range(1, flipcount + 1):
                    usedlist[xpos][ypos + k] = 1
        if (len(usedlist) - (xpos + 1)) <= (len(usedlist[xpos]) - (ypos + 1)):
            templimits = (len(usedlist) - (xpos + 1))
        else:
            templimits = (len(usedlist[xpos]) - (ypos + 1))
        flipcount = 0
        for h in range(1, templimits):
            if usedlist[xpos + h][ypos + h] == 0:
                break
            if usedlist[xpos + h][ypos + h] == 2:
                flipcount += 1
            if usedlist[xpos + h][ypos + h] == 1:
                for k in range(1, flipcount + 1):
                    usedlist[xpos + k][ypos + k] = 1
        if xpos + 1 <= (len(usedlist[xpos]) - (ypos + 1)):
            templimits = xpos - 1
        else:
            templimits = (len(usedlist[xpos]) - (ypos + 1))
        flipcount = 0
        for h in range(1, templimits):
            if usedlist[xpos - h][ypos + h] == 0:
                break
            if usedlist[xpos - h][ypos + h] == 2:
                flipcount += 1
            if usedlist[xpos - h][ypos + h] == 1:
                for k in range(1, flipcount + 1):
                    usedlist[xpos - k][ypos + k] = 1
        if xpos + 1 <= ypos + 1:
            templimits = xpos - 1
        else:
            templimits = ypos - 1
        flipcount = 0
        for h in range(1, templimits):
            if usedlist[xpos - h][ypos - h] == 0:
                break
            if usedlist[xpos - h][ypos - h] == 2:
                flipcount += 1
            if usedlist[xpos - h][ypos - h] == 1:
                for k in range(1, flipcount + 1):
                    usedlist[xpos - k][ypos - k] = 1
        if (len(usedlist) - (xpos + 1)) <= ypos + 1:
            templimits = (len(usedlist) - (xpos + 1))
        else:
            templimits = ypos + 1
        flipcount = 0
        for h in range(1, templimits):
            if usedlist[xpos + h][ypos - h] == 0:
                break
            if usedlist[xpos + h][ypos - h] == 2:
                flipcount += 1
            if usedlist[xpos + h][ypos - h] == 1:
                for k in range(1, flipcount + 1):
                    usedlist[xpos + k][ypos - k] = 1

    return usinglist


xpiece = []
ypiece = []
blackwhitelist = []



input = "c 3 1 7 2 2 2 1"
inputlist = input.split()
if inputlist[0] == "a":
    usinglist = lista
if inputlist[0] == "b":
    usinglist = listb
if inputlist[0] == "c":
    usinglist = listc
for i in range(1, int(inputlist[1]) + 1):
    xpiece.append(int(inputlist[i * 2]))
    ypiece.append(int(inputlist[(i * 2) + 1]))
for i in range(int(inputlist[1])):
    blackwhitelist.append(i)



for i in range(len(xpiece)):
    for j in range(len(usinglist)):
        print((getmoves(xpiece[i] - 1, ypiece[i] - 1, usinglist, blackwhitelist[i]))[j])
    print("---------------------------------")
whitecount = 0
blackcount = 0
for i in range(len(usinglist)):
    for j in range(len(usinglist)):
        if usinglist[i][j] == 0:
            pass
        if usinglist[i][j] == 1:
            whitecount += 1
        if usinglist[i][j] == 2:
            blackcount += 1
print(whitecount)
print(blackcount)
