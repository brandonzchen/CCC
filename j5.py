import sys

minimum = int(sys.stdin.readline())
maximum = int(sys.stdin.readline())
numnewlocations = int(sys.stdin.readline())

unsortedmotels = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]
ways = [1]
count = 0

for i in range(numnewlocations):
    tempnewlocation = int(sys.stdin.readline())
    unsortedmotels.append(tempnewlocation)
sortedmotels = sorted(unsortedmotels)

for i in sortedmotels:
    if i  - minimum < 0:
        pass
    if i > minimum:
        tempmin = i - maximum
        tempmax = i - minimum
        if tempmax > minimum or tempmin < maximum:
            for j in range(tempmin, tempmax + 1):
                if j in sortedmotels:
                    count += ways[sortedmotels.index(j)]
        ways.append(count)
        count = 0

final = len(ways) - 1
print(ways[final])
