from sys import argv

script, filename = argv
file = open(filename, "r")
n=int(file.readline())
first=file.readline()
second=file.readline()

#n=int(input('How many spaces? '))
#first=[]
#second=[]
count=0
for i in range(n):
    if first[i]=='C' and second[i]=='C':
        count=count+1
    else:
        pass
print(count)
#p=0
#while n>p:
    #if first[(n-1)-p]=='C' and second[(n-1)-p]=='C':
        #count=count+1
    #else:
        #pass
    #p=p+1
#print(count)
