import sys
finallist = []
originallist = [1, 2, 3, 4, 5, 6, 7]
taskconditions = [[7,2],[4,5],[1,7],[1,4],[2,1],[3,4],[3,5]]
orderdic = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[]}

# reading input
# inputcondition = 0
# tempinputlist =[]
# while True:
#     inputs = sys.stdin.readline()
#     if inputs != 0:
#         tempinputlist.append(inputs)
#         if len(tempinputlist) == 2:
#             taskconditions.append(tempinputlist)
#             tempinputlist = []
#     if inputs == 0:
#         break


for i, j in taskconditions:
    orderdic[i].append(j)
originallist = {1, 2, 3, 4, 5, 6, 7}
def getmoves(useddic, finalorder):
    templist = []
    for i in useddic:
        for j in useddic[i]:
            templist.append(j)
    setmoves = set(templist)
    availablemoves = list(originallist - setmoves)
    smallest = 8
    for i in availablemoves:
        if i < smallest:
            smallest = i
    if smallest == 8:
        print("Cannot complete these tasks. Going to bed.")
        sys.exit()
    originallist.remove(smallest)
    finalorder.append(smallest)
    del(useddic[smallest])
    return useddic

temp = getmoves(orderdic, finallist)
for i in range(6):
    temp = getmoves(temp, finallist)
#getmoves(getmoves(getmoves(getmoves(getmoves(getmoves(getmoves(orderdic, finallist), finallist), finallist), finallist), finallist), finallist), finallist)
for i in finallist:
    print(i, end =" ")
