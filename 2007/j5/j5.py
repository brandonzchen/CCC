import sys

minimum = 970
maximum = 1040
# numnewlocations = int(sys.stdin.readline())

# int(sys.stdin.readline())

unsortedmotels = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]
# unsortedmotels = [0,1,2,3,4,5,6,7,8,9,10]


# for i in range(numnewlocations):
#     tempnewlocation = int(sys.stdin.readline())
#     unsortedmotels.append(tempnewlocation)
sortedmotels = sorted(unsortedmotels)
ways = [0 for i in range(len(sortedmotels))]
ways[0] = 1
enumerated = list(enumerate(sortedmotels))
print(enumerated)
for i in sortedmotels:
    count = 0
    if i < minimum:
        pass
    if i >= minimum:
        tempmin = i - maximum
        tempmax = i - minimum
        for j, h in enumerated:
            if h >= tempmin and h <= tempmax:
                count += ways[j]
        ways[sortedmotels.index(i)] = count
print(ways)
print(ways[-1])
