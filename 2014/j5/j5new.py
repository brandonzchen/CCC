import sys
numberpeople = int(sys.stdin.readline())
input = sys.stdin.readline()
firstgroup = input.split()
input = sys.stdin.readline()
secondgroup = input.split()
# numberpeople = 7
# firstgroup = ["Rich", "Graeme", "Michelle", "Sandy", "Vlado", "Ron", "Jacob"]
# secondgroup = ["Ron", "Vlado", "Sandy", "Michelle", "Rich", "Graeme", "Jacob"]

pairdict = {}
for i in firstgroup:
    pairdict.setdefault(i)
for i in range(len(secondgroup)):
    pairdict[firstgroup[i]] = (secondgroup[i])
condition = 0
for i in pairdict:
    if i == pairdict[i]:
        condition = 1
        break
    else:
        if i != pairdict[pairdict[i]]:
            condition = 1
            break
if condition == 1:
    print("bad")
else:
    print("good")
