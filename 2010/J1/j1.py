input = 4
count = 0
if input <= 5:
    count += 1
for _i_ in range(1,input):
    if input % 2 == 0:
        if input - _i_ >= input // 2  and input - _i_ <= 5:
            count += 1
    if input % 2 != 0:
        if input - _i_ >= (input // 2) + 1 and input - _i_ <= 5:
            count += 1
print(count)
