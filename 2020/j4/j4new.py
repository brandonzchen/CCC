import sys
file = open("C:\\Users\\brand\\Desktop\\CCC\\2020\\j4\\j4.06.01.in", "r")

input = file.readline()

search = file.readline().strip()
# input = sys.stdin.readline().strip()
# search = sys.stdin.readline().strip()

shiftslist = []
for i in range(len(search)):
    templist = []
    templist.append(search[i:])
    templist.append(search[:i])
    tempstr = ""
    tempstr = "".join(templist)
    shiftslist.append(tempstr)
window = len(search)

for i in shiftslist:
    if i in input:
        print("yes")

# templist = []
# totallist = []
# for i in range(len(input)):
#     for j in range(window):
#         if i + j < len(input):
#             templist.append(input[i + j])
#     tempstr = ""
#     tempstr = "".join(templist)
#     totallist.append(tempstr)
#     templist = []
# print(totallist)
# condition = 0
# for i in shiftslist:
#     if i in totallist:
#         condition = 1
#         break
# if condition == 1:
#     print("yes")
# if condition == 0:
#     print("no")
