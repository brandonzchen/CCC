
file = open("C:\\Users\\brand\\Desktop\\CCC\\2013\\J5\\j5.2.in", "r")

favorite = int(file.readline())
matches = int(file.readline())
# 1 3 5 7
# 3 4 8 0
# 2 4 2 2
# 1 2 5 5
matchesplayed = []
teamsdict = {1: 0, 2: 0, 3: 0, 4: 0}
for i in range(matches):
    linestr = file.readline()
    linestr = linestr.split()
    line = []
    for j in linestr:
        line.append(int(j))
    firsteam = line[0]
    secondteam = line[1]
    if line[2] > line[3]:
        teamsdict[line[0]] += 3
    if line[2] < line[3]:
        teamsdict[line[1]] += 3
    if line[2] == line[3]:
        teamsdict[line[0]] += 1
        teamsdict[line[1]] += 1
    temp = []
    temp.append(line[0])
    temp.append(line[1])
    matchesplayed.append(temp)
print(teamsdict)
totalmatches = []
for i in range(1, 5):
    for j in range(1, 5):
        if j > i:
            temp = []
            temp.append(i)
            temp.append(j)
            totalmatches.append(temp)
matchesleft = []
for i in totalmatches:
    if i not in matchesplayed:
        matchesleft.append(i)
print(matchesleft)
print(favorite)
remaining = []
for i in range(1, 4):
    for j in range(1, 4):
        for h in range(1, 4):
            for t in range(1, 4):
                for g in range(1, 4):
                    temp = []
                    temp.append(i)
                    temp.append(j)
                    temp.append(h)
                    temp.append(t)
                    temp.append(g)
                    remaining.append(temp)
possiblecount = 0
print(remaining)
notfavorite = []
for t in range(1, 5):
    if t != favorite:
        notfavorite.append(t)
for i in remaining:
    condition = 0
    tempcopy = teamsdict.copy()
    for j in i:
        if j == 1:
            tempcopy[matchesleft[i.index(j)][0]] += 3
        elif j == 3:
            tempcopy[matchesleft[i.index(j)][0]] += 1
            tempcopy[matchesleft[i.index(j)][1]] += 1
        elif j == 2:
            tempcopy[matchesleft[i.index(j)][1]] += 3
    print(tempcopy)
    if tempcopy[favorite] > tempcopy[1] and tempcopy[favorite] > tempcopy[3] and tempcopy[favorite] > tempcopy[4]:
        possiblecount += 1



print(possiblecount)
