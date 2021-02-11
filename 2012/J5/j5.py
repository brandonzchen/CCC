linecount = 0
numbercoins = []
totalcoinorder = []
targetsorder = []



def moveright(usedlist, position):

    templist = []
    for i in usedlist:
        temp = i.copy()
        templist.append(temp)
    current = templist[position]
    lastitem = templist[position][0]
    del(templist[position][0])
    templist[position + 1].insert(0, lastitem)
    return templist




def moveleft(usedlist, position):

    templist = []
    for i in usedlist:
        temp = i.copy()
        templist.append(temp)
    current = templist[position]
    lastitem = templist[position][0]
    del(templist[position][0])
    templist[position - 1].insert(0, lastitem)
    return templist



def getmoves(usedlist):
    newlayer = []

    for i in usedlist:
        for j in i:
            if len(j) == 0:
                pass
            else:
                currentindex = i.index(j)
                # check the moves possible to the right when the next box has value
                if currentindex != len(i) - 1 and len(i[currentindex + 1]) != 0 and \
                    j[0] < i[currentindex + 1][0]:
                    temporary = moveright(i, currentindex)
                    if temporary not in newlayer:
                        newlayer.append(temporary)
                # check the moves when the next box has no value
                if currentindex != len(i) - 1 and len(i[currentindex + 1]) == 0:
                    temporary = moveright(i, currentindex)
                    if temporary not in newlayer:
                        newlayer.append(temporary)

                # check the moves possible to the left when the next box has value
                if currentindex != 0 and len(i[currentindex - 1]) != 0 and \
                    j[0] < i[currentindex - 1][0]:
                    temporary = moveleft(i, currentindex)
                    if temporary not in newlayer:
                        newlayer.append(temporary)
                # check the moves when the next box has no value
                if currentindex != 0 and len(i[currentindex - 1]) == 0:
                    temporary = moveleft(i, currentindex)
                    if temporary not in newlayer:
                        newlayer.append(temporary)

    return newlayer



#
#
file = open("C:\\Users\\brand\\Desktop\\CCC\\2012\\J5\\j5.3.in", "r")
n = int(file.readline())
targetsorder = []
while n > 0:
    coinorder = []
    temp = file.readline().split()
    temp = list(map(int, temp))
    for i in temp:
        coinorder.append([i])
    totalcoinorder.append([coinorder])
    numbercoins.append(n)
    targetsorder.append([[i] for i in range(1, len(coinorder) + 1)])
    n = int(file.readline())

#
# n = int(input())
# targetsorder = []
# while n > 0:
#     coinorder = []
#     temp = input().split()
#     temp = list(map(int, temp))
#     for i in temp:
#         coinorder.append([i])
#     totalcoinorder.append([coinorder])
#     numbercoins.append(n)
#     targetsorder.append([[i] for i in range(1, len(coinorder) + 1)])
#     n = int(input())

for i in range(len(totalcoinorder)):
    visited = []
    tempqueued = []
    queued = totalcoinorder[i]
    target = targetsorder[i]
    # print(target)
    count = 0
    condition = 0
    while target not in visited and target not in queued:
        tempqueued = []
        for u in range(len(queued)):
            order = queued[0]
            visited.append(order)
            queued.remove(order)
            temp = getmoves([order])
            for tempnew in temp:
                if tempnew not in queued and tempnew not in visited:
                    queued.append(tempnew)
        for i in tempqueued:
            queued.append(i)

        count += 1

        if len(queued) == 0:
            print('IMPOSSIBLE')
            condition = 1
            break

    if condition == 0:
        print(count)
