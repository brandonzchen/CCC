from sys import argv

script, filename = argv
file = open(filename, "r")
number=(file.readline())
votes=(file.readline())

x=votes.count('A')
y=votes.count('B')

if x>y:
    print('A')
if y>x:
    print('B')
if x==y:
    print('Tie')
