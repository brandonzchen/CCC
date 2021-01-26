# input
# 3
# 2 2 3
# 0
# 0


pagesdict = {}
file = open("C:\\Users\\brand\\Desktop\\CCC\\2018\\J5\\j5.3-1.in", "r")
pages = int(file.readline())
for i in range(1, pages + 1):
    line = file.readline()
    line = line.split()
    if line[0] == "0":
        pagesdict.setdefault(i,[0])
    else:
        temp = []
        for j in range(1, int(line[0]) + 1):
            temp.append(int(line[j]))
        pagesdict.setdefault(i, temp)





visited = []
queued = []
for i in pagesdict[1]:
    queued.append(i)
visited.append(1)
temp1 = []
for i in queued:
    for j in pagesdict[i]:
        if j == 0:
            pass
        else:
            temp1.append(j)
    visited.append(i)
shortest = []
count = 0
def getnext(useddict, usedqueue, usedvisited, shortcount):
    temp = []
    for i in usedqueue:
        for j in useddict[i]:
            if j == 0:
                shortest.append(shortcount)
                pass
            else:
                temp.append(j)
        usedvisited.append(i)
    usedqueue = temp
    shortcount += 1
    return usedqueue
for i in range(20):
    if i == 0:
        current = getnext(pagesdict, temp1, visited, count)
    else:
        current = getnext(pagesdict, current, visited, count)
print(list(set(shortest)))
print(list(set(visited)))
compare = []
for i in range(1, 1001):
    compare.append(i)
if compare == list(set(visited)):
    print("yes")
else:
    print("no")
