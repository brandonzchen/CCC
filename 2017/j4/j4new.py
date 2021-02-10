# starting time = 12:00 or 0 minutes
# total = starting time + input = 34
import sys
originalinput = int(sys.stdin.readline())
if originalinput == 0:
    print(0)
else:
    overcount = 0
    totalcount = []
    finallist = []
    if originalinput > 720:
        input = originalinput % 720
        overcount = originalinput // 720
    else:
        input = originalinput
    if input <= 59 and input >= 34:
        totalcount.append(1)
    else:
        timelist = [12, 00]
        while input > 59:
            if timelist[1] + input > 59:
                if timelist[0] == 12:
                    timelist[0] = 1
                else:
                    timelist[0] += 1
                input -= 60
        timelist[1] += input
        clocktimes = []
        for i in range(1, 10):
            for j in range(6):
                for h in range(10):
                    if h - j == j - i:
                        temp = []
                        temp.append(i)
                        temp.append((j * 10) + h)
                        clocktimes.append(temp)
        clocktimes.append([11, 11])
        clocktimes.append([12, 34])
        hourbased = []
        for i in clocktimes:
            if i[0] < timelist[0] + 1:
                hourbased.append(i)
        for i in hourbased:
            if i[0] < timelist[0]:
                finallist.append(i)
            if i[0] == timelist[0]:
                if i[1] <= timelist[1]:
                    finallist.append(i)
        if originalinput >= 34:
            finallist.append([12, 34])
    totalcount.append(overcount * 31)
    totalcount.append(len(finallist))
    count = 0
    for i in totalcount:
        count += i
    print(count)
