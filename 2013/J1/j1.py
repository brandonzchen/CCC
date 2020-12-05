from sys import argv

script, filename = argv
file = open(filename, "r")
first=int(file.readline())
second=int(file.readline())

x=second-first
y=x+second
print(y)
