from sys import argv

script, filename = argv
file = open(filename, "r")
first=int(file.readline())
second=int(file.readline())
third=int(file.readline())
for i in range(1): 
    if first==second==third and first+second+third==180:
        print("Equilateral")
        break
    if first+second+third!=180:
        print("Error")
        break
    if first==second or first==third or second==third and first+second+third==180:
        print("Isoceles")
        break
    if first!=second!=third and first+second+third==180:
        print("Scalene")
        break
