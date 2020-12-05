from sys import argv

script, filename = argv
file = open(filename, "r")
drops=int(file.readline())
x=[]
y=[]
for i in range(drops):
    cord=file.readline().split(',')
    cord[1].rstrip('\n')  
    x.append(cord[0])
    y.append(cord[1])
     
x.sort()
y.sort()
t=int(drops-1)

print(str(int(x[0])-1)+','+str(int(y[0])-1))
print(str(int(x[t])+1)+','+str(int(y[t])+1))







