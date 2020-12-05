import sys
from sys import argv

script, filename = argv
file = open(filename, "r")
l=[]
for i in range(4):
    l.append(file.readline().split())

#script, filename = argv
#file = open(filename, "r")
#l=[]
#l=file.read().splitlines()
print(l)
rowsum=0
n=len(l)
print (n)
for i in range(n):
    temp=0
    for j in range(n):
        temp+=int(l[i][j])
    if rowsum==0:
        rowsum=temp
    elif rowsum!=temp:
        print('not magic')
        exit()

for i in range(n):
    temp=0
    for j in range(n):
        temp+=int(l[j][i])
    if rowsum!=temp:
        print('not magic')
        exit()
    if i==n-1:
        print('magic')
