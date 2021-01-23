import sys
input = "01:00"
minutes = 0
for i in range(len(input)):
    if i == 0:
        minutes += int(input[i]) * 600
    if i == 1:
        minutes += int(input[i]) * 60
    if i == 2:
        pass
    if i == 3:
        minutes += int(input[i]) * 10
    if i == 4:
        minutes += int(input[i])
# 7 to 10 and 15 to 19 is rush hour
morningstart = 420
morningend = 600
nightstart = 900
nightend = 1140
totaltime = 0
if minutes >= morningstart and minutes < morningend:
    rushtime = morningend - minutes
    normaltime = 120 - int(rushtime / 2)
    totaltime = rushtime + normaltime + minutes
    if rushtime > 240:
        totaltime = 240
if minutes < morningstart and minutes + 120 > morningstart:
    normaltime = morningstart - minutes
    rushtime = (120 - normaltime) * 2
    totaltime = normaltime + rushtime + minutes
if minutes >= nightstart and minutes < nightend:
    rushtime = nightend - minutes
    normaltime = 120 - int(rushtime / 2)
    totaltime = rushtime + normaltime + minutes
    if rushtime > 240:
        totaltime = 240
if minutes < nightstart and minutes + 120 > nightstart:
    normaltime = nightstart - minutes
    rushtime = (120 - normaltime) * 2
    totaltime = normaltime + rushtime + minutes



if minutes < morningstart and minutes + 120 < morningstart:
    totaltime = minutes + 120
if minutes > morningend and minutes + 120 < nightstart:
    totaltime = minutes + 120
if minutes > nightend:
    totaltime = minutes + 120
if totaltime >= 1440:
    totaltime = totaltime - 1440
endtime = []
if totaltime // 60 > 9:
    endtime.append(str(totaltime // 60))
else:
    endtime.append("0")
    endtime.append(str(totaltime // 60))
endtime.append(":")
if totaltime % 60 > 9:
    endtime.append(str(totaltime % 60))
else:
    endtime.append("0")
    endtime.append(str(totaltime % 60))
for i in endtime:
    print(i, end = "")










# if minutes >= morningstart and minutes < morningend:
#     rushtemp = morningend - minutes
#     realrush = int(rushtemp / 2)
#     if realrush < 120:
#         normaltemp = 120 - realrush
#         totaltemp = normaltemp + rushtemp
#         print(totaltemp)
#     if realrush > 120:
#         print(240)
# if minutes < morningstart and (minutes + 120) > morningstart:
#     normaltemp = morningstart - minutes
#     rushtemp = 120 - normaltemp
#     realrush = rushtemp * 2
#     totaltemp = normaltemp + realrush
#     print(totaltemp)
