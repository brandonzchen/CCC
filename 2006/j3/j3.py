alphabet = [["a","b","c"], ["d","e","f"], ["g","h","i"],["j","k","l"],["m","n","o"], ["p","q","r","s"], ["t","u","v"], ["w","x","y","z"]]
input = "abracadabra"
wordlist = []
for i in input:
    for j in range(8):
        if i in alphabet[j]:
            templist = []
            templist.append(j)
            templist.append(alphabet[j].index(i))
            wordlist.append(templist)
previousvalue = -1
totalcount = 0
for f,g in wordlist:
    if g == 0:
        totalcount += 1
    if g == 1:
        totalcount += 2
    if g == 2:
        totalcount +=3
    if g == 3:
        totalcount +=4
    if previousvalue == -1:
        previousvalue = f
    elif f == previousvalue:
        totalcount += 2
    if f != previousvalue:
        previousvalue = f
print(totalcount)
