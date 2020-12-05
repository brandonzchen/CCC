pos=[]
upcount=0
downcount=0
for i in range(4):
    x=int(sys.stdin.readline())
    pos.append(x)
for i in range(3):
    if pos[i]<pos[i+1]:
        upcount+=1
    if pos[i]>pos[i+1]:
        downcount+=1
if upcount==3:
    print("Fish Rising")
elif downcount==3:
    print("Fish Diving")
elif upcount==0 and downcount==0:
    print("Fish At Constant Depth")
else:
    print("No Fish")
