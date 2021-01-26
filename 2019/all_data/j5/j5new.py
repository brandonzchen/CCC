import sys


def rep(origine, searchdict, totallist, indexlist, rulelist):
    temptotallist = []
    tempindexlist = []
    temprulelist = []
    for t in searchdict:
        search = searchdict[t][0]
        replace = searchdict[t][1]
        window = len(search)
        windowlist = []
        templist = []
        for i in range(len(origine)):
            for j in range(window):
                if i + j < len(origine):
                    templist.append(origine[i + j])
            if len(templist) == window:
                tempstr = ""
                tempstr = tempstr.join(templist)
                windowlist.append(tempstr)
                templist = []
        for j in range(len(windowlist)):
            if windowlist[j] == search:
                left = origine[0:j]
                middle = replace
                right = origine[j + len(search): len(origine) + len(search)]
                total = left + middle + right
                tempindexlist.append(j + 1)
                temptotallist.append(total)
                temprulelist.append(t)
    deletinglist = []
    visited = []
    for h in range(len(temptotallist)):
        if h in deletinglist:
            pass
        else:
            for m in range(len(temptotallist)):
                if m != h:
                    if temptotallist[h] == temptotallist[m]:
                        deletinglist.append(m)

    for i in range(len(temptotallist)):
        if i not in deletinglist:
            totallist.append(temptotallist[i])
            indexlist.append(tempindexlist[i])
            rulelist.append(temprulelist[i])

    return totallist
file = open("C:\\Users\\brand\\Desktop\\CCC\\2019\\all_data\j5\j5.10.in", "r")
searchdict = {}
# print(file.read())

for i in range(3):
    tempfile = file.readline()
    tempfile = tempfile.split()
    searchdict.setdefault(i + 1, [tempfile[0], tempfile[1]])
tempfile = file.readline()
tempfile = tempfile.split()
numbersteps = int(tempfile[0])
start = tempfile[1]
total = tempfile[2]

print(searchdict)
print(start)
print(total)

list = []
rules = []
index = []
first = rep(start, searchdict, list, index, rules)
letterslists = []
indexlists = []
rulelists = []
letterslists.append(list)
indexlists.append(index)
rulelists.append(rules)
previoustotal = list
print(letterslists)
print(indexlists)
print(rulelists)
for h in range(numbersteps):
    temptotal = []
    temprules = []
    tempindex = []
    for i in previoustotal:
        temp = []
        for j in rep(i, searchdict, temp, tempindex, temprules):
            temptotal.append(j)
    letterslists.append(temptotal)
    indexlists.append(tempindex)
    rulelists.append(temprules)
    previoustotal = temptotal
letterslists.reverse()
indexlists.reverse()
rulelists.reverse()





endsteps = []
for i in range(numbersteps + 1):
    tempend = []
    target = total
    for j in letterslists[i]:
        if j == target:
            break
    targetindex = letterslists[i].index(j)
    numberindex = indexlists[i][targetindex]
    numberrule = rulelists[i][targetindex]
    tempend.append(numberrule)
    tempend.append(numberindex)
    rulelist = searchdict[numberrule]
    left = target[0:numberindex -  1]
    middle = rulelist[0]
    right = target[(numberindex - 1) + len(rulelist[1]):]
    total = left + middle + right
    tempend.append(total)
    endsteps.append(tempend)
endsteps.reverse()

for i in range(len(endsteps)):
    if i + 1 < len(endsteps):
        tempsteps = []
        tempsteps.append(endsteps[i][0])
        tempsteps.append(endsteps[i][1])
        tempsteps.append(endsteps[i+1][2])
        print(*tempsteps)
