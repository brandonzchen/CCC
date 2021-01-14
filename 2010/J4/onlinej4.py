from math import ceil
f = open('C://Users//brand//Desktop/CCC/2010/J4/j4.4.in')
while True:
    user_input = f.readline().split()
    print(user_input)
    length = int(user_input[0])
    if length == 0:
        break
    numbers = [int(x) for x in user_input[1:]]
    changes = []
    previous_value = 0
    for i, v in enumerate(numbers):
        if i > 0:
            changes.append(v - previous_value)
        previous_value = v
    if len(changes) == 0:
        print(numbers[0])
    print(changes)
    for x in range(1, len(changes) + 1):
        cycle = changes[:x]
        print(cycle)
        new_cycle = cycle * ceil(len(changes) / x)
        print(new_cycle)
        if new_cycle[:len(changes)] == changes:
            print(x)
            break
