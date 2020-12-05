from sys import argv

script, filename = argv
file = open(filename, "r")
games=int(file.readline())
gamescoresA=[]
gamescoresD=[]
david=100
antonia=100

for i in range(games):
    score=file.readline()
    f=score.split()
    gamescoresA.append(f[0])
    gamescoresD.append(f[1])
for i in range(len(gamescoresA)):
    if gamescoresA[i]>gamescoresD[i]:
        david=david-int(gamescoresA[i])
    if gamescoresD[i]>gamescoresA[i]:
        antonia=antonia-int(gamescoresD[i])
print(antonia)
print(david)

               
    
    
