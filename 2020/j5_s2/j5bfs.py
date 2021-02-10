



# rows = int(input())
# columns = int(input())
# array = []
# for i in range(rows):
#     temp = []
#     line = input()
#     line = line.split()
#     for j in line:
#         temp.append(int(j))
#     array.append(temp)
# #
file =  open("C:\\Users\\brand\\Desktop\\CCC\\2020\\j5_s2\\j5.06.03.in", "r")

rows = int(file.readline())
columns = int(file.readline())
array = []
for i in range(rows):
    temp = []
    line = file.readline()
    line = line.split()
    for j in line:
        temp.append(int(j))
    array.append(temp)




target = rows * columns
pathways = [-1 for i in range(10 * rows * columns)]


# condition = False
count = 0
totalcount = 1
pathways[count] = array[0][0]
condition = 0
while target not in pathways:
    if pathways[count] == -1:
        condition = 1
        break
    for i in range(rows):
        # if target % (i + 1) == 0:
        for j in range(int(target // (i + 1)) + 1):
            if (i + 1) * (j + 1) == pathways[count]:
                if i <= rows - 1 and j <= columns - 1:
                    if array[i][j] not in pathways:
                        pathways[totalcount] = array[i][j]
                        totalcount += 1
    count += 1
# print(pathways)
if condition == 1:
    print("no")
else:
    print("yes")
