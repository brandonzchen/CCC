import itertools

# numberpieces = int(input())
# boardnumbers = input()
# boardnumbers = boardnumbers.split()
# for i in range(numberpieces):
#     boardnumbers[i] = int(boardnumbers[i])



# 1, 2, 3, 4, 5, 6

numbers = [1, 2, 3, 4, 5, 6]
list1 = itertools.permutations(numbers, 2)
combinations = list(list1)
# print(combinations)
doublecombinations = itertools.combinations_with_replacement(combinations, 3)
finallist = list(doublecombinations)
working = []
for i in finallist:
    if i[0][0] + i[0][1] == i[1][0] + i[1][1] and i[0][0] + i[0][1] == i[2][0] + i[2][1]:
        working.append(i)

print(working)
