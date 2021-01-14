def getmoves(startx, starty):
    movelist = [[2, -1], [2, 1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
    return_pos = []
    for i in range(8):
        if startx + movelist[i][0] <= 8 and startx + movelist[i][0] >= 1:
            if starty + movelist[i][1] <= 8 and starty + movelist[i][1] >= 1:
                temp=[]
                temp.append(startx + movelist[i][0])
                temp.append(starty + movelist[i][1])
                return_pos.append(temp)
    return return_pos


startpos = [8, 8]
endpos = [1, 1]
count = 1

visited = getmoves(startpos[0], startpos[1])
visited.append(startpos)
print(visited)
count = 1
result = 0
for visited_pos in visited:
    count += 1
    for item in getmoves(visited_pos[0], visited_pos[1]):
        
        if item == endpos:
            result = count
            break
        elif item not in visited:
            visited.append(item)
    if result > 0:
        break
print(result)




    # for _i_ in movelist1:
    #     for _j_ in movelist2:
    #         if startx + _i_ <= 7 and startx + _i_ >= 0:
    #             if starty + _j_ <= 7 and starty + _j_ >= 0:
    #                 temp = []
    #                 temp.append(startx + _i_)
    #                 temp.append(starty + _j_)
    #                 endxy.append(temp)
    # for _i_ in movelist2:
    #     for _j_ in movelist1:
    #         if startx + _i_ <= 7 and startx + _i_ >= 0:
    #             if starty + _j_ <= 7 and starty + _j_ >= 0:
    #                 temp = []
    #                 temp.append(startx + _i_)
    #                 temp.append(starty + _j_)
    #                 endxy.append(temp)
