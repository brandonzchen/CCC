import sys
minormax = int(sys.stdin.readline())
numberofpeople = int(sys.stdin.readline())
input = sys.stdin.readline()
city1input = input.split()
city1 = []
for i in city1input:
    city1.append(int(i))



input = sys.stdin.readline()
city2input = input.split()
city2 = []
for i in city2input:
    city2.append(int(i))

# numberofpeople = 3
# minormax = 1
# city1 = [5,1,4]
# city2 = [6,2,4]
# pairs = []
def mingetpairs(list1, list2, pairspeed):
    temp1 = 0
    for i in list1:
        if i > temp1:
            temp1 = i
    temp2 = 0
    for j in list2:
        if j > temp2:
            temp2 = j
    if temp2 > temp1:
        pairspeed.append(temp2)
    else:
        pairspeed.append(temp1)
    list1.remove(temp1)
    list2.remove(temp2)
def maxgetpairs(list1, list2, pairspeed):
    temp1 = 0
    for i in list1:
        if i > temp1:
            temp1 = i
    temp2 = list2[0]
    for j in list2:
        if j < temp2:
            temp2 = j
    if temp1 > temp2:
        pairspeed.append(temp1)
    else:
        pairspeed.append(temp2)
    list1.remove(temp1)
    list2.remove(temp2)
if minormax == 1:
    for i in range(numberofpeople):
        mingetpairs(city1, city2, pairs)
if minormax == 2:
    for i in range(numberofpeople):
        maxgetpairs(city1, city2, pairs)
total = 0
for i in pairs:
    total += i
print(total)
