import sys
x=int(sys.stdin.readline())
firstline=["*","x","*"]
secondline=[" ","x","x"]
thirdline=["*"," ","*"]
for i in range(x):
    print(firstline[0]*x+firstline[1]*x+firstline[2]*x)
for i in range(x):
    print(secondline[0]*x+secondline[1]*x+secondline[2]*x)
for i in range(x):
    print(thirdline[0]*x+thirdline[1]*x+thirdline[2]*x)
