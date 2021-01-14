forwardbackward = [4,2,5,3]
steps = 12
nikkycount = 0
byroncount = 0
temptotal = 0
loopbreak = 0
while loopbreak == 0:
    temptotal += forwardbackward[0]
    if (temptotal) <= steps:
        nikkycount += forwardbackward[0]
    temptotal += forwardbackward[1]
    if (temptotal + forwardbackward[1]) <= steps:
        nikkycount -=forwardbackward[1]
    if temptotal > steps:
        loopbreak += 1
print(nikkycount)
