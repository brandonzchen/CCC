# file = open("C:\\Users\\brand\\Desktop\\CCC\\2012\\J4\\j4.1.in", "r")
alphabet=[]
alphabet = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
shiftnumber=int(input())
word=input().strip()
final=[]
x=1
for i in word:
    shiftspace=(3*x)+shiftnumber
    index=alphabet.index(i)
    index-=shiftspace
    if index<0:
        while index<0:
            index+=26
    final.append(alphabet[index])
    x+=1
print(''.join(final))
