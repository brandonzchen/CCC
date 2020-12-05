from sys import argv

script, filename = argv
file = open(filename, "r")
x=int(file.readline())
names1=file.readline().split()
names2=file.readline().split()
p=0
result='good'
while p<x and result=='good':
    temp=names1.index(names2[p])
    if names1[p]!=names2[temp] or temp==p:
        result='bad'
    p+=1
print(result)
     
