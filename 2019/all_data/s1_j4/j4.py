from sys import argv

script, filename = argv
file = open(filename, "r")
filestring=file.readline()
print(filestring)
gridshape=[1,2,3,4]
vcount=0
hcount=0
for char in filestring:
    if char =='V':
        vcount+=1
    elif char=='H':
        hcount+=1
    else:
        pass
if vcount % 2 != 0 and hcount % 2 != 0:
    print(gridshape[3],gridshape[2])
    print(gridshape[1],gridshape[0])
elif vcount % 2 !=0 and hcount % 2 == 0:
    print(gridshape[1],gridshape[0])
    print(gridshape[3],gridshape[2])
elif vcount % 2 == 0 and hcount % 2 !=0:
    print(gridshape[2],gridshape[3])
    print(gridshape[0],gridshape[1])
else:
    print(gridshape[0],gridshape[1])
    print(gridshape[2],gridshape[3])

    

