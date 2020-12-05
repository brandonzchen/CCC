import sys
alphabet=[]
alphabet = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
shiftnumber=9
word="WWWXXXYYYZZZ"
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
