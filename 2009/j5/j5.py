import sys
friendsdict = {1:[6], 2:[6], 3:[4, 5, 6, 15], 4:[3, 5, 6], 5:[3, 4, 6],
                6:[1, 2, 3, 4, 5, 7], 7:[6, 8], 8:[7, 9], 9:[8, 10, 12],
                10:[9, 11], 11:[10, 12], 12:[9, 11, 13], 13:[12, 15, 14],
                14:[13], 15:[3, 13], 16:[17, 18], 17:[16, 18], 18:[16, 17]}
# i x y makes x and y friends, no output
# d x y deletes friendship between, no output
# n x outputs number of friends x has
# f x outputs number fo friends of friend x has
# s x y outputs degree/shortest paths, if not connected, print notconnected
# q quit program
input = ["i", 20, 10, "i", 20, 9, "n", 20, "f", 20, "s", 20, 6, "q"]
def actioni(useddict, friend1, friend2):
    if friend1 in useddict[friend2]:
        pass
    if friend1 not in useddict:
        useddict.setdefault(friend1, [])
        useddict[friend1].append(friend2)
        useddict[friend2].append(friend1)
    if friend2 not in useddict:
        useddict.setdefault(friend2, [])
        useddict[friend2].append(friend1)
        useddict[friend1].append(friend2)
    if friend1 not in useddict[friend2]:
        useddict[friend1].append(friend2)
        useddict[friend2].append(friend1)
def actiond(useddict, friend1, friend2):
    useddict[friend1].remove(friend2)
    useddict[friend2].remove(friend1)
def actionn(useddict, person):
    print(len(useddict[person]))
def actionf(useddict, person):
    foff = []
    for i in useddict[person]:
        for j in useddict[i]:
            if j not in useddict[person] and j not in foff and j != person:
                foff.append(j)
    print(len(foff))
def actions(useddict, friend1, friend2):
    visited = []
    queued = [[friend2]]
    tempqueued = []
    for i in queued:
        for j in i:
            if j not in useddict:
                break
            else:
                for h in useddict[j]:
                    if h not in tempqueued:
                        tempqueued.append(h)
        visited.append(i)
        queued.append(tempqueued)
        tempqueued = []
        condition = 0
        for t in visited:
            if friend1 in t:
                queued = []
        condition = 1
        if condition == 1:
            queued = []
    if condition == 1:
        print('Not Connected')
    if condition == 0:
        print(visited.index(t) - 1)


f = open("C:\\Users\\brand\\Desktop\\CCC\\2009\\j5\\j5_1.txt", "r")
for i in range(50):
    tempinput = f.readline()
    for i in range(len(tempinput)):
        if i == 0:
            tempinput = tempinput[i]
    if tempinput == "i":
        first = int(f.readline())
        second = int(f.readline())
        actioni(friendsdict, first, second)
    if tempinput == "d":
        first = int(f.readline())
        second = int(f.readline())
        actiond(friendsdict, first, second)
    if tempinput == "n":
        first = int(f.readline())
        actionn(friendsdict, first)
    if tempinput == "f":
        first = int(f.readline())
        actionf(friendsdict, first)
    if tempinput == "s":
        first = int(f.readline())
        second = int(f.readline())
        actions(friendsdict, first, second)
    if tempinput == "q":
        break
