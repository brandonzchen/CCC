# welcome is 7 letters
# to is 2 letters
# ccc is 3 letters
# good is 4 letters
# luck is 4 letters
# today is 5 letters
from math import ceil

input = 15

letterslist = [7, 2, 3, 4, 4, 5]
templetterstotal = 0
endphrase = []
lines = []
spacecount = 0
for i in letterslist:
    templetterstotal += i
    if templetterstotal + spacecount <= input:
        lines.append(i)
        spacecount += 1
    if templetterstotal + spacecount > input:
        endphrase.append(lines)
        lines = []
        spacecount = 0
        lines.append(i)
        templetterstotal = i
endphrase.append(lines)
print(endphrase)
spaceslist = []
for i in endphrase:
    letterlinetotal = 0
    for j in i:
        letterlinetotal += j
    spacecount = input - letterlinetotal
    tempspaces = []
    if len(i) - 1 != 0:
        tempspaces.append((ceil(spacecount / (len(i) - 1))))
        tempspaces.append(spacecount - (ceil(spacecount / (len(i) - 1))))
        spaceslist.append(tempspaces)
    if len(i) - 1 == 0:
        tempspaces.append(spacecount)
        spaceslist.append(tempspaces)
    tempspaces = []
print(spaceslist)
stringlist = ["WELCOME", "TO", "CCC", "GOOD", "LUCK", "TODAY"]
# for i in endphrase:
#     for j in range(len(i)):
#         print(stringlist[j], end = " ")
#         stringlist.remove(stringlist[j])
