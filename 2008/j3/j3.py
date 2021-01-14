alphabetlist = [["A", "B", "C", "D", "E", "F"],
                ["G", "H", "I", "J", "K", "L"],
                ["M", "N", "O", "P", "Q", "R"],
                ["S", "T", "U", "V", "W", "X"],
                ["Y", "Z", " ", "-", ".", "Enter"]]

inputstring = "ECHO ROCK"
indexlist = [[0,0]]
tempindex = []
for item in inputstring:
    for _i_ in range(5):
        if item in alphabetlist[_i_]:
            tempindex.append(_i_)
            tempindex.append(alphabetlist[_i_].index(item))
            indexlist.append(tempindex)
            tempindex = []
indexlist.append([4, 5])
total = 0
for _j_ in range(len(indexlist)-1):
    if indexlist[_j_][0] > indexlist[_j_ + 1][0]:
        total += indexlist[_j_][0] - indexlist[_j_ + 1][0]
    if indexlist[_j_][0] <= indexlist[_j_ + 1][0]:
        total += indexlist[_j_ + 1][0] - indexlist[_j_][0]
    if indexlist[_j_][1] > indexlist[_j_ + 1][1]:
        total += indexlist[_j_][1] - indexlist[_j_ + 1][1]
    if indexlist[_j_][1] <= indexlist[_j_ + 1][1]:
        total += indexlist[_j_ + 1][1] - indexlist[_j_][1]
print(total)
