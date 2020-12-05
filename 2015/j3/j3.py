import sys
listvowels=["a","e","i","o","u"]
consonants=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z","z"]
cA=["b","c"]
cE=["d","f","g"]
cI=["h","j","k","l"]
cO=["m","n","p","q","r"]
cU=["s","t","v","w","x","y","z"]
word = "jazz"
x=list(word.strip())
final=[]
for i in range(len(x)):
    if x[i] in listvowels:
        final.append(x[i])
    if x[i] in consonants:
        final.append(x[i])
        if x[i] in cA:
            final.append("a")
        if x[i] in cE:
            final.append("e")
        if x[i] in cI:
            final.append("i")
        if x[i] in cO:
            final.append("o")
        if x[i] in cU:
            final.append("u")
        index=consonants.index(x[i])
        final.append(str(consonants[index+1]))
j=""
for i in final:
    j+=i
print(j)
