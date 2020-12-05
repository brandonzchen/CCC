from sys import argv

script, filename = argv
file = open(filename, "r")
l=[]
l=file.read().splitlines()
numbers=[]
for item in l:
    for i in item.split():
        numbers.append(i)
print(numbers)
x=0
newnumbers1=[]
while x<15:
    temp=int(numbers[x])+int(numbers[x+1])+int(numbers[x+2])+int(numbers[x+3])
    newnumbers1.append(temp)
    x+=4
print(newnumbers1)
p=0
newnumbers2=[]
while p<4:
    temp=int(numbers[p])+int(numbers[p+4])+int(numbers[p+8])+int(numbers[p+12])
    newnumbers2.append(temp)
    p+=1
print(newnumbers2)
if newnumbers1[0]==newnumbers1[1] and newnumbers1[0]==newnumbers1[2] and newnumbers1[0]==newnumbers1[3]:
    if newnumbers1==newnumbers2:
        print('magic')
else:
    print('not magic')
