from sys import argv
import sys
def pal(n):
    for i in range(len(n)//2):
        if n[-1-i]!=n[i]:
            result=0
            break
        else:
            result=len(n)
    return result
input='abcbabct'
#for j in range(len(input)):
    #for i in range(j+1):
        #temp=input[i:i+len(input)-j]
        #if pal(temp)>0:
            #print(pal(temp))
            #exit()
for x in range(len(input)):
    temp=input[x:len(input)-x]
    len(input)-=1
    print(temp)
