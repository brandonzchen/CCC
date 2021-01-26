import sys
starting = [[1, 2], [3, 4]]
def horizontal(usedlist):
    usedlist.append(usedlist[0])
    del(usedlist[0])
def vertical(usedlist):
    usedlist[0].append(usedlist[0][0])
    del(usedlist[0][0])
    usedlist[1].append(usedlist[1][0])
    del(usedlist[1][0])
input = sys.stdin.readline()
for i in input:
    if i == "H":
        horizontal(starting)
    if i == "V":
        vertical(starting)
for i in starting[0]:
    print(i, end = " ")
print()
for j in starting[1]:
    print(j, end = " ")
