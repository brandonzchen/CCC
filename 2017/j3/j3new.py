import sys


startpos = []
endpos = []


firstline = sys.stdin.readline()
firstline = firstline.split()
for i in firstline:
    startpos.append(int(i))
secondline = sys.stdin.readline()
secondline = secondline.split()
for i in secondline:
    endpos.append(int(i))
ecount = int(sys.stdin.readline())

firstdis = startpos[0] - endpos[0]
seconddis = startpos[1] - endpos[1]
if firstdis < 0:
    firstdis = firstdis * (-1)
if seconddis < 0:
    seconddis = seconddis * (-1)
totaldis = firstdis + seconddis
condition = 0
if ecount - totaldis >= 0 and (ecount - totaldis) % 2 == 0:
    condition += 1
else:
    pass
if ecount - totaldis < 0:
    pass
if condition == 0:
    print("N")
else:
    print("Y")
