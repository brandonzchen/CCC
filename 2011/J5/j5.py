frienddict = {}
numberoffriends = 6
for i in range(1, numberoffriends + 1):
    frienddict.setdefault(i, 1)
input = [4,4,5,6,6]
print(frienddict)
for i in range(1, numberoffriends):
    temp = input[i - 1]
    frienddict[temp] = frienddict[temp] * (frienddict[i] + 1)
print(frienddict)
