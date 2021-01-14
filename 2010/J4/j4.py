from math import ceil
# practicelist = [3, 4, 6, 4, 5, 7, 5]
differencelist = [1, 3, 1, 4, 1, 5, 1, 4]
referencelist = []
for i in differencelist:
    referencelist.append(i)
    new_reference = referencelist * ceil(len(differencelist)/(len(referencelist)))
    print(new_reference)
    if new_reference[:len(differencelist)] == differencelist:
        print("happy")
