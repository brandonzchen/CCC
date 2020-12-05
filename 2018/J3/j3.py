from sys import argv
script, filename = argv
file = open(filename, "r")
#city=file.readline()
l=[]
l=file.readline().split()
l.insert(0,0)
p=0
for i in range(len(l)):
    l[i]=int(l[i])
    p=p+l[i]
p=l[0]+l[1]+l[2]+l[3]+l[4]
x=p
for i in range(5):
    x=x-int(l[i])
    print(abs(p-x),abs(x-(int(l[4])+int(l[3])+int(l[2]))),abs(x-(int(l[4])+int(l[3]))),abs(x-int(l[4])),abs(x-int(l[0])))

#for i in range(5):
    #x=x+l[i]
    #print(x,abs(x-l[1]),abs(x-(l[1]+l[2])),abs(x-(l[1]+l[2]+l[3])),abs(x-(l[1]+l[2]+l[3]+l[4])))
