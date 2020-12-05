from sys import argv

script, filename = argv
file = open(filename, "r")
directions=[]
y=0
count=0
for i in range(4):
    temp=(file.readline())
    x=temp.split()
    if temp=='':
        y=1
    else:
        directions.append(x)
        count+=1
floorplan=[]
floorplan.append([0,-1])
floorplan.append([0,-2])
floorplan.append([0,-3])
floorplan.append([1,-3])
floorplan.append([2,-3])
floorplan.append([3,-3])
floorplan.append([3,-4])
floorplan.append([3,-5])
floorplan.append([4,-5])
floorplan.append([5,-5])
floorplan.append([5,-4])
floorplan.append([5,-3])
floorplan.append([6,-3])
floorplan.append([7,-3])
floorplan.append([7,-4])
floorplan.append([7,-5])
floorplan.append([7,-6])
floorplan.append([7,-7])
floorplan.append([6,-7])
floorplan.append([5,-7])
floorplan.append([4,-7])
floorplan.append([3,-7])
floorplan.append([2,-7])
floorplan.append([1,-7])
floorplan.append([0,-7])
floorplan.append([-1,-7])
floorplan.append([-1,-6])
floorplan.append([-1,-5])
start=[-1,-5]


for i in range(count):
    status="safe"
    if directions[i][0]=='l':
        for j in range(int(directions[i][1])):
            start[0]-=1
            if start in floorplan:
                status='DANGER'
            floorplan.append(start)
        print(start,status)

    if directions[i][0]=='d':
        for j in range(int(directions[i][1])):
            start[1]-=1
            if start in floorplan:
                status='DANGER'    
        print(start,status)
    if directions[i][0]=='r':
        for j in range(int(directions[i][1])):
            start[0]+=1
            if start in floorplan:
                status='DANGER'    
        print(start,status)
    if directions[i][0]=='u':
        for j in range(int(directions[i][1])):
            start[1]+=1
            if start in floorplan:
                status='DANGER'    
        print(start,status)
    if directions[i][0]=='q':
        quit()

    






                 
