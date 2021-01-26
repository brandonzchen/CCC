import sys

def getmoves(startgrid, currentmoves, pastmoves):
    delindex = []
    combinationswithout = []
    for h in pastmoves:
        for i in range(1, startgrid[h[0] - 1][h[1] - 1] + 1):
            for j in range(1, startgrid[h[0] - 1][h[1] - 1] + 1):
                if i * j == startgrid[h[0] - 1][h[1] - 1]:
                    temp = []
                    temp.append(i)
                    temp.append(j)
                    currentmoves.append(temp)
                    for t in range(len(currentmoves)):
                        if currentmoves[t][0] > rownumber or currentmoves[t][1] > columnnumber:
                            delindex.append(t)
                    for f in range(len(currentmoves)):
                        if f not in delindex:
                            combinationswithout.append(currentmoves[f])
    pastmoves = combinationswithout
    return pastmoves

def function(combinations):
    condition = 0
    for i in range(3):
        if i == 0:
            current = getmoves(input, combinations, possiblelist)
            combinations = []
            for j in current:
                if j == [rownumber, columnnumber]:
                    condition = 1
                    return condition
        else:
            current = getmoves(input, combinations, current)
            combinations = []
            for j in current:
                if j == [rownumber, columnnumber]:
                    condition = 1
                    return condition

file = open("C:\\Users\\brand\\Desktop\\CCC\\2020\\j5_s2\\j5.01.06.in", "r")
input = []
rownumber = int(file.readline())
columnnumber = int(file.readline())
for i in range(rownumber):
    temp = []
    line = file.readline()
    line = line.split()
    for j in line:
        temp.append(int(j))
    input.append(temp)
print(input)


# input = []
# rownumber = int(sys.stdin.readline())
# columnnumber = int(sys.stdin.readline())
# for i in range(rownumber):
#     temp = []
#     line = sys.stdin.readline()
#     line = line.split()
#     for j in line:
#         temp.append(int(j))
#     input.append(temp)



possiblelist = [[1,1]]
start = input[0][0]
end = input[rownumber - 1][columnnumber - 1]
combinations = []


for h in possiblelist:
    for i in range(1, input[h[0]][h[1]] + 1):
        for j in range(1, input[h[0]][h[1]] + 1):
            if i * j == input[h[0]][h[1]]:
                temp = []
                temp.append(i)
                temp.append(j)
                combinations.append(temp)


if function(combinations) == 1:
    print("yes")
else:
    print("no")

# combinations = []
# for h in possiblelist:
#     for i in range(1, input[h[0] - 1][h[1] - 1] + 1):
#         for j in range(1, input[h[0] - 1][h[1] - 1] + 1):
#             if i * j == input[h[0] - 1][h[1] - 1]:
#                 temp = []
#                 temp.append(i)
#                 temp.append(j)
#                 combinations.append(temp)
#                 for t in range(len(combinations)):
#                     if combinations[t][0] > rownumber or combinations[t][1] > columnnumber:
#                         del(combinations[t])
