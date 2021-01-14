totalboxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
boxesopened = [3, 4, 5, 6, 7, 8, 9, 10]
bankersdeal = 400
moneylist = []
for i in boxesopened:
    totalboxes.remove(i)
for j in totalboxes:
    if j == 1:
        moneylist.append(100)
    if j == 2:
        moneylist.append(500)
    if j == 3:
        moneylist.append(1000)
    if j == 4:
        moneylist.append(5000)
    if j == 5:
        moneylist.append(10000)
    if j == 6:
        moneylist.append(25000)
    if j == 7:
        moneylist.append(50000)
    if j == 8:
        moneylist.append(100000)
    if j == 9:
        moneylist.append(500000)
    if j == 10:
        moneylist.append(1000000)
total = 0
for h in moneylist:
    total += h
if total / len(moneylist) > bankersdeal:
    print("no deal")
else:
    print("deal")
