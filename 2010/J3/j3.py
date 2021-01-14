
A = 0
B = 0
inputlist = ["1 A 3", "1 B 4", "2 B", "2 A", "3 A B", "2 A", "5 A A", "2 A", "2 B", "7"]
functionslist = [1, 2, 3, 4, 5, 6, 7]
for listcount in range(len(inputlist)):
    if inputlist[listcount][0] == "1":
        if inputlist[listcount][2] == "A":
            A = int(inputlist[listcount][4])
        if inputlist[listcount][2] == "B":
            B = int(inputlist[listcount][4])
    if inputlist[listcount][0] == "2":
        if inputlist[listcount][2] == "A":
            print(A)
        if inputlist[listcount][2] == "B":
            print(B)
    if inputlist[listcount][0] == "3":
        if inputlist[listcount][2] == "A" and inputlist[listcount][4] == "A":
            A = A + A
        if inputlist[listcount][2] == "A" and inputlist[listcount][4] == "B":
            A = A + B
        if inputlist[listcount][2] == "B" and inputlist[listcount][4] == "B":
            A = B + B
        if inputlist[listcount][2] == "B" and inputlist[listcount][4] == "A":
            A = B + A
    if inputlist[listcount][0] == "4":
        if inputlist[listcount][2] == "A" and inputlist[listcount][4] == "A":
            A = A * A
        if inputlist[listcount][2] == "A" and inputlist[listcount][4] == "B":
            A = A * B
        if inputlist[listcount][2] == "B" and inputlist[listcount][4] == "B":
            A = B * B
        if inputlist[listcount][2] == "B" and inputlist[listcount][4] == "A":
            A = B * A
    if inputlist[listcount][0] == "5":
        if inputlist[listcount][2] == "A" and inputlist[listcount][4] == "A":
            A = A - A
        if inputlist[listcount][2] == "A" and inputlist[listcount][4] == "B":
            A = A - B
        if inputlist[listcount][2] == "B" and inputlist[listcount][4] == "B":
            A = B - B
        if inputlist[listcount][2] == "B" and inputlist[listcount][4] == "A":
            A = B - A
    if inputlist[listcount][0] == "6":
        if inputlist[listcount][2] == "A" and inputlist[listcount][4] == "A":
            A = A // A
        if inputlist[listcount][2] == "A" and inputlist[listcount][4] == "B":
            A = A // B
        if inputlist[listcount][2] == "B" and inputlist[listcount][4] == "B":
            A = B // B
        if inputlist[listcount][2] == "B" and inputlist[listcount][4] == "A":
            A = B // A
    if inputlist[listcount][0] == "7":
        break
