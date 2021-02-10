linecount = 0
numbercoins = []
totalcoinorder = []
targetsorder = []
# while True:
#     if linecount % 2 == 0:
#         coins = int(input())
#         if coins == 0:
#             break
#         else:
#             numbercoins.append(coins)
#     if linecount % 2 != 0:
#         coinorder = []
#         reversecoinorder = []
#         tempcoinorder = input()
#         tempcoinorder = tempcoinorder.split()
#         for i in tempcoinorder:
#             coinorder.append([int(i)])
#         final = [coinorder]
#         totalcoinorder.append(final)
#         for j in range(1, len(tempcoinorder) + 1):
#             reversecoinorder.append([j])
#         targetsorder.append(reversecoinorder)
#     linecount += 1

file = open("C:\\Users\\brand\\Desktop\\CCC\\2012\\J5\\j5.2.in", "r")
while True:
    if linecount % 2 == 0:
        coins = int(file.readline())
        if coins == 0:
            break
        else:
            numbercoins.append(coins)
    if linecount % 2 != 0:
        coinorder = []
        reversecoinorder = []
        tempcoinorder = file.readline()
        tempcoinorder = tempcoinorder.split()
        for i in tempcoinorder:
            coinorder.append([int(i)])
        final = [coinorder]
        totalcoinorder.append(final)
        for j in range(1, len(tempcoinorder) + 1):
            reversecoinorder.append([j])
        targetsorder.append(reversecoinorder)
    linecount += 1





def moveright(usedlist, position):
    # templist = usedlist.copy()
    # current = templist[position]
    # lastitem = current[len(current) - 1]
    # del(current[len(current) - 1])
    # templist[position + 1].append(lastitem)
    # return templist
    templist = []
    for i in usedlist:
        temp = i.copy()
        templist.append(temp)
    current = templist[position]
    lastitem = templist[position][-1]
    del(templist[position][-1])
    templist[position + 1].append(lastitem)
    return templist




def moveleft(usedlist, position):
    # templist = usedlist.copy()
    # current = templist[position]
    # lastitem = current[len(current) - 1]
    # del(current[len(current) - 1])
    # templist[position - 1].append(lastitem)


    templist = []
    for i in usedlist:
        temp = i.copy()
        templist.append(temp)
    current = templist[position]
    lastitem = templist[position][-1]
    del(templist[position][-1])
    templist[position - 1].append(lastitem)
    return templist

#
# print(moveleft(coinorder, 2))
# print(coinorder)
#
def getmoves(usedlist):
    newlayer = []
    # for i in usedlist:
    #     for j in i:
    #         currentindex = i.index(j)
    #         if (currentindex + 1) <= len(i) - 1:
    #             if j[-1] < i[i.index(j) + 1][-1]:
    #                 newlayer.append(moveright(i, currentindex))
    #         if (currentindex - 1) >= 0 and (currentindex - 1) <= len(i) - 1:
    #             if j[-1] < i[i.index(j) - 1][-1]:
    #                 newlayer.append(moveleft(i, currentindex))
    # return newlayer
    for i in usedlist:
        for j in i:
            if len(j) == 0:
                pass
            else:
                currentindex = i.index(j)
                if currentindex + 1 < len(i):
                    if len(i[currentindex + 1]) != 0:
                        if i[currentindex][-1] < i[currentindex + 1][-1]:
                            temporary = moveright(i, currentindex)
                            if temporary not in newlayer:
                                newlayer.append(moveright(i, currentindex))
                    else:
                        temporary = moveright(i, currentindex)
                        if temporary not in newlayer:
                            newlayer.append(moveright(i, currentindex))
                if currentindex > 0:
                    if len(i[currentindex - 1]) != 0:
                        if i[currentindex][-1] < i[currentindex - 1][-1]:
                            temporary = moveleft(i, currentindex)
                            if temporary not in newlayer:
                                newlayer.append(moveleft(i, currentindex))
                    else:
                        temporary = moveleft(i, currentindex)
                        if temporary not in newlayer:
                            newlayer.append(moveleft(i, currentindex))

    return newlayer

for u in totalcoinorder:
    visited = []
    queued = u
    target = targetsorder[totalcoinorder.index(u)]
    count = -1
    condition = 0
    while target not in visited:
        count += 1
        for i in queued:
            visited.append(i)
            queued.remove(i)
            temp = getmoves([i])
            for j in temp:
                if j not in queued and j not in visited:
                    queued.append(j)
        if len(queued) == 0:
            print('IMPOSSIBLE')
            condition = 1
            break
    if condition == 0:
        print(count)


# count = 0
# addingcount = 0
# visited[count] = coinorder[0]
# while target not in visited:
#     temp = getmoves([visited[count]])
#     for i in temp:
#         if i not in visited:
#             visited[addingcount] = i
#             addingcount += 1
#     if visited[addingcount] == -1:
#         print(visited)
#         break



# x = getmoves(coinorder)
# for i in x:
#     print(i)
#     if i not in visited:
#         visited[addingcount] = i
#         addingcount += 1
# print(visited)
#
# x = getmoves(coinorder)
#
# print(getmoves(x))
#
# y = getmoves(x)
#
# print(getmoves(y))
