# from sys import argv
#
# script, filename = argv
# file = open(filename, "r")
# first=int(file.readline())
# second=int(file.readline())

# 0 in ottawa
# victoria -300
# edmonton -200
# winnipeg -100
# toronto -0
# halifax +100
# st. johns +130
def timefinder(z):
    templist=list(map(int, str(z)))
    if len(templist)==4 and templist[2]>=6:
        z=z+41
        newtimes.append(z)
        z=0
        templist=[]
    if len(templist)==3 and templist[1]>=6:
        z=z+41
        newtimes.append(z)
        z=0
        templist=[]
    if len(templist)==2 and templist[0]>=6:
        z=z+41
        newtimes.append(z)
        z=0
        templist=[]
    else:
        newtimes.append(z)
        z=0


x=17
y=list(map(int, str(x)))
times=[-300,-200,-100,0,100,130]
newtimes=[]
temp=0

for i in range(6):
    if times[i]+x<2359 and times[i]+x>0:
        temp=times[i]+x
        timefinder(temp)
    if times[i]+x>2359:
        temp=(times[i]+x)-2359
        timefinder(temp)
    if x+times[i]<0:
        temp=2359+(times[i]+x)
        timefinder(temp)
print(newtimes)



# templist=list(map(int, str(temp)))
# if len(templist)==4 and templist[2]>=6:
#     temp=temp+41
#     newtimes.append(temp)
#     temp=0
#     templist=[]
#     continue
# if len(templist)==3 and templist[1]>=6:
#     temp=temp+41
#     newtimes.append(temp)
#     temp=0
#     templist=[]
#     continue
# if len(templist)==2 and templist[0]>=6:
#     temp=temp+41
#     newtimes.append(temp)
#     temp=0
#     templist=[]
#     continue
# else:
#     newtimes.append(temp)
#     temp=0
