import sys
# inputm = int(sys.stdin.readline())
# inputn = int(sys.stdin.readline())
inputm = 12
inputn = 4
tencount = 0
for i in range(1, inputm + 1):
    for j in range(1, inputn + 1):
        if i + j == 10:
            tencount += 1
print(tencount)
