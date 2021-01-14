originalorder = ["A", "B", "C", "D", "E"]
buttonfunctions = [2, 3, 2, 4]
buttonpresses = [1, 1, 3, 1]

for _i_ in range(len(buttonfunctions)):
    for _j_ in range(buttonpresses[_i_]):
        if buttonfunctions[_i_] == 1:
            originalorder.append(originalorder[0])
            del originalorder[0]
        if buttonfunctions[_i_] == 2:
            originalorder.insert(0, originalorder[4])
            del originalorder[4]
        if buttonfunctions[_i_] == 3:
            originalorder.append(originalorder[0])
            del originalorder[0]
            originalorder.insert(0, originalorder[4])
            del originalorder[4]

print(originalorder)
