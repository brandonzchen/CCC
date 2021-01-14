import sys
foodlist = [2,1,3,4]
# for i in range(4):
#     foodlist.append(int(sys.stdin.readline()))
enumerated = list(enumerate(foodlist))
caloriecount = 0
for j,v in enumerated:
    if j == 0:
        if v == 1:
            caloriecount += 461
        if v == 2:
            caloriecount += 431
        if v == 3:
            caloriecount += 420
        if v == 4:
            caloriecount += 0
    if j == 1:
        if v == 1:
            caloriecount += 100
        if v == 2:
            caloriecount += 57
        if v == 3:
            caloriecount += 70
        if v == 4:
            caloriecount += 0
    if j == 2:
            if v == 1:
                caloriecount += 130
            if v == 2:
                caloriecount += 160
            if v == 3:
                caloriecount += 118
            if v == 4:
                caloriecount += 0
    if j == 3:
            if v == 1:
                caloriecount += 167
            if v == 2:
                caloriecount += 266
            if v == 3:
                caloriecount += 75
            if v == 4:
                caloriecount += 0
print(caloriecount)
