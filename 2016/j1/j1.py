from sys import argv

script, filename = argv
file = open(filename, "r")
l=[]
l=file.read().splitlines()

for item in l:
    for i in item.split():
        print(i)


print(type(l))

count=0
for item in l:
    if item=='W':
        count+=1
print (count)

if int(count)==5 or int(count)==6:
    print(1)
elif int(count)==4 or int(count)==3:
    print(2)
elif int(count)==1 and int(count)==2:
    print(3)
else:
    print(-1)
