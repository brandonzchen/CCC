firststring = "MATH CLASS"
secondstring = "LAST CHASM"
firstlist = []
secondlist = []
for i in firststring:
    if i != " ":
        firstlist.append(i)
for j in secondstring:
    if j != " ":
        secondlist.append(j)
print(firstlist)
print(secondlist)
sorted1 = sorted(firstlist)
sorted2 = sorted(secondlist)
print(sorted1)
print(sorted2)
if sorted1 == sorted2:
    print("Is an anagram.")
else:
    print("Is not an anagram")
