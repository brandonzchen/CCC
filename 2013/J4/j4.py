from sys import argv

script, filename = argv
file = open(filename, "r")
time=int(file.readline())
chorenum=int(file.readline())
chores=[]
for i in range(chorenum):
    temp=int(file.readline())
    chores.append(temp)

chores.sort()
realtime=chores[0]
listnumber=0
while realtime<=time:
    listnumber+=1
    realtime+=chores[listnumber]
print(listnumber)
    
    
