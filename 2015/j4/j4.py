
numberlist=[]
timelist=[]
wtime=0
ttime=0
testl=["R 12","W 2","R 23","W 3","R 45","S 23","R 23","W 2","S 23","R 34","S 12","S 34"]
for i in range(12):
    temp=testl[i]
    templ=temp.split()
    if templ[0]=="S" or templ[0]=="R":
        ttime+=wtime
        timelist.append(ttime)
        numberlist.append(int(templ[1]))
        wtime=0
        ttime+=1
    else:
        wtime=int(templ[1])-1
dict={}
for i in range(len(numberlist)):
    x=numberlist[i]
    dict.setdefault(x,[]).append(timelist[i])
x=sorted(list(set(numberlist)))
print(dict)
def addsub(dictlists):
    if len(dictlists)%2==1:
        return -1
    else:
        for i in range(len(dictlists)):
            if i%2==0:
                dictlists[i]=dictlists[i]*-1
        total=0
        for item in dictlists:
            total+=item
        return total
for i in x:
    print(i, addsub(dict[i]))
