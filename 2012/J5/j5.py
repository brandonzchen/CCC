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


# while True:
#     if linecount % 2 == 0:
#         coins = int(file.readline())
#         if coins == 0:
#             break
#         else:
#             numbercoins.append(coins)
#     if linecount % 2 != 0:
#         coinorder = []
#         reversecoinorder = []
#         tempcoinorder = file.readline()
#         tempcoinorder = tempcoinorder.split()
#         for i in tempcoinorder:
#             coinorder.append([int(i)])
#         totalcoinorder.append([coinorder])
#         # targetsorder = [[i] for i in range(1, len(tempcoinorder) + 1)]
#         for j in range(1, len(tempcoinorder) + 1):
#             reversecoinorder.append([j])
#         targetsorder.append(reversecoinorder)
#     linecount += 1




# targetsorder = [[i] for i in range(1, len(tempcoinorder) + 1)]



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
    lastitem = templist[position][0]
    del(templist[position][0])
    templist[position + 1].insert(0, lastitem)
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
    lastitem = templist[position][0]
    del(templist[position][0])
    templist[position - 1].insert(0, lastitem)
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
                # check the moves possible to the right when the next box has value
                if currentindex != len(i) - 1 and len(i[currentindex + 1]) != 0 and \
                    j[0] < i[currentindex + 1][0]:
                    temporary = moveright(i, currentindex)
                    if temporary not in newlayer:
                        newlayer.append(moveright(i, currentindex))
                # check the moves when the next box has no value
                elif currentindex != len(i) - 1 and len(i[currentindex + 1]) == 0:
                    temporary = moveright(i, currentindex)
                    if temporary not in newlayer:
                        newlayer.append(moveright(i, currentindex))

                # check the moves possible to the left when the next box has value
                if currentindex != 0 and len(i[currentindex - 1]) != 0 and \
                    j[0] < i[currentindex - 1][0]:
                    temporary = moveleft(i, currentindex)
                    if temporary not in newlayer:
                        newlayer.append(moveleft(i, currentindex))
                # check the moves when the next box has no value
                elif currentindex != 0 and len(i[currentindex - 1]) == 0:
                    temporary = moveleft(i, currentindex)
                    if temporary not in newlayer:
                        newlayer.append(moveleft(i, currentindex))

                print(newlayer, "newlayer")
    return newlayer
    # for i in usedlist:
    #     for j in i:
    #         if len(j) == 0:
    #             pass
    #         else:
    #             thisindex = i.index(j)
    #             if thisindex + 1 < len(i):
    #                 if j[-1] < i[thisindex + 1][-1] or len(i[thisindex + 1]) == 0:
    #                     thismove = moveright(i, thisindex)
    #                     if thismove not in newlayer:
    #                         newlayer.append(thismove)
    #             if thisindex > 0:
    #                 if j[-1] < i[thisindex - 1][-1] or len(i[thisindex - 1]):
    #                     thismove = moveleft(i, thisindex)
    #                     if thismove not in newlayer:
    #                         newlayer.append(thismove)




file = open("C:\\Users\\brand\\Desktop\\CCC\\2012\\J5\\j5.1.in", "r")
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


print(totalcoinorder)
print(targetsorder)

for i in range(len(totalcoinorder)):
    visited = []
    queued = totalcoinorder[i]
    target = targetsorder[i]
    # print(target)
    count = 0
    condition = 0
    while target not in visited and target not in queued:
        for order in queued:
            visited.append(order)
            queued.remove(order)
            temp = getmoves([order])
            for tempnew in temp:
                if tempnew not in queued and tempnew not in visited:
                    queued.append(tempnew)
        print(queued, count, '_________')
        print(visited, count, '0000000')
        count += 1
        # if target in visited or target in queued:
        #     break

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
