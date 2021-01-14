def getmoves(startx, starty, endxy):
    movelist1 = [-2, 2]
    movelist2 = [-1, 1]
    for _i_ in movelist1:
        for _j_ in movelist2:
            if startx + _i_ <= 7 and startx + _i_ >= 0:
                if starty + _j_ <= 7 and starty + _j_ >= 0:
                    temp = []
                    temp.append(startx + _i_)
                    temp.append(starty + _j_)
                    endxy.append(temp)
    for _i_ in movelist2:
        for _j_ in movelist1:
            if startx + _i_ <= 7 and startx + _i_ >= 0:
                if starty + _j_ <= 7 and starty + _j_ >= 0:
                    temp = []
                    temp.append(startx + _i_)
                    temp.append(starty + _j_)
                    endxy.append(temp)
    return endxy


allmoves = []
temporarymoves = []

realendpos = [2, 2]
realstartpos = [1, 1]
endpos = [realendpos[0]-1,realendpos[1]-1]
count = 1
getmoves(realstartpos[0]-1, realstartpos[1]-1, allmoves)
while endpos not in allmoves:
    for i in range(len(allmoves)):
        for j in range(len(getmoves(allmoves[i][0], allmoves[i][1], temporarymoves))):
            if temporarymoves[j] not in allmoves:
                allmoves.append(temporarymoves[j])
    count += 1
print(count)
print(allmoves)
