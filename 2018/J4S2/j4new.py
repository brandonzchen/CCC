import sys
input = []

# file = open("C:\\Users\\brand\\Desktop\\CCC\\2018\\J4S2\\s2.02.in", "r")
# numberlines = int(file.readline())
# for i in range(numberlines):
#     temp = []
#     line = file.readline()
#     line = line.split()
#     for j in range(numberlines):
#         temp.append(int(line[j]))
#     input.append(temp)


numberlines = int(sys.stdin.readline())
for i in range(numberlines):
    temp = []
    line = sys.stdin.readline()
    line = line.split()
    for j in range(numberlines):
        temp.append(int(line[j]))
    input.append(temp)
# print(input)

# 4 3 1
# 6 5 2
# 9 7 3
# input = [[1, 3], [2, 9]]
def turn90(usedlist, newlist):
    for i in range(len(usedlist)):
        temp = []
        for j in range(len(usedlist)):
            temp.append(usedlist[j][len(usedlist) - i - 1])
        newlist.append(temp)
    return(newlist)

def test(nextlist):
    condition = 0
    for i in range(len(nextlist)):
        for j in range(len(nextlist[i])):
            if j == 0:
                currentcompare = nextlist[i][j]
            else:
                if nextlist[i][j] > currentcompare:
                    currentcompare = nextlist[i][j]
                else:
                    condition = 1
                    return condition
    for i in range(len(nextlist)):
        if i == 0:
            currentcompare = nextlist[i][0]
        else:
            if nextlist[i][0] > currentcompare:
                currentcompare = nextlist[i][0]
            else:
                condition = 1
                return condition
    for i in range(len(nextlist)):
        if i == 0:
            currentcompare = nextlist[i][len(nextlist[i]) - 1]
        else:
            if nextlist[i][len(nextlist[i]) - 1] > currentcompare:
                currentcompare = nextlist[i][len(nextlist[i]) - 1]
            else:
                condition = 1
                return condition
    return condition

rotated = []
nextstep = []

if test(rotated) == 1:
    print(turn90(rotated, nextstep))
rotated = []
nextstep = []
target = []
for i in range(4):
    turn90(input, nextstep)
    if test(nextstep) == 0:
        target = nextstep
        break
    else:
        pass
    input = nextstep
    nextstep = []
for i in target:
    for j in range(len(i)):
        print(i[j], end = " ")
    print()
