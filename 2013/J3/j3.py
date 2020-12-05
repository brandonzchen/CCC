from sys import argv

script, filename = argv
file = open(filename, "r")
first=int(file.readline())


def FindDupe(lists):
    a=set(lists)
    if len(a)<len(lists):
        return False
    else:
        return True
        

first+=1
    
while not FindDupe([int(x) for x in str(first)]):
    first+=1

print(first)




