import sys
chorestime = []
timeallowed = int(sys.stdin.readline())
chores = int(sys.stdin.readline())
for i in range(chores):
    temp = int(sys.stdin.readline())
    chorestime.append(temp)
totaltime = 0
chorescount = 0
chorestime.sort()
for i in chorestime:
    if (i + totaltime) <= timeallowed:
        totaltime += i
        chorescount += 1
print(chorescount)
