def getmoves(startx, starty, endxy):
    movelist = [[2, -1], [2, 1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
    for i in range(8):
        if startx + movelist[i][0] <= 8 and startx + movelist[i][0] >= 1:
            if starty + movelist[i][1] <= 8 and starty + movelist[i][1] >= 1:
                temp=[]
                temp.append(startx + movelist[i][0])
                temp.append(starty + movelist[i][1])
                endxy.append(temp)
    return endxy


startpos = [8, 8]
endpos = [1, 1]
count = 1
visited = [startpos]
temporarymoves = []
getmoves(startpos[0], startpos[1], visited)
while endpos not in visited:
    for i in range(len(visited)):
        for item in getmoves(visited[i][0], visited[i][1], temporarymoves):
            if item not in visited:
                visited.append(item)
    count += 1
print(count)
