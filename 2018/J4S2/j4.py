from sys import argv
import copy

def rotateRight(origin,k):
    result=copy.deepcopy(origin)
    for i in range(k):
        for j in range(k):
            result[j][k-i-1]=int(origin[i][j])
    return result

script, filename = argv
file = open(filename, "r")
n=int(file.readline())
l=[]
for i in range(n):
    l.append(file.readline().split())


#x=rotateRight(rotateRight(l,n),n)
#print(l)
#print(x)
max=max(l[0][0],l[0][n-1],l[n-1][0],l[n-1][n-1])
if max==l[n-1][n-1]:
    print(l)
elif max==l[0][n-1]:
    oneturn=rotateRight(l,n)
    print(oneturn)
elif max==l[0][0]:
    twoturn=rotateRight(rotateRight(l,n),n)
    print(twoturn)
else:
    threeturn=rotateRight(rotateRight(rotateRight(l,n),n),n)
    print(threeturn)




#if l[n-1][n-1]>l[0][0] and l[n-1][n-1]>l[0][n-1] and l[n-1][n-1]>l[n-1][0]:
#    print(l)
#elif l[0][n-1]>l[0][0] and l[0][n-1]>l[n-1][n-1] and l[0][n-1]>l[n-1][0]:
#    oneturn=rotateRight(l,n)
#    print('x')
#elif l[0][0]>l[n-1][n-1] and l[0][0]>l[n-1][0] and l[0][0]>l[0][n-1]:
#    twoturn=rotateRight(rotateRight(l,n),n)
#    print(twoturn)
#else:
#    threeturn=rotateRight(rotateRight(rotateRight(l,n),n),n)
#    print(threeturn)
