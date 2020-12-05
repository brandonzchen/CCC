#from sys import argv

#script, filename = argv
#file = open(filename, "r")
#first=file.readline()
import itertools

string = 'aaab'
s = set()
for p in itertools.permutations(string):
    s.add(p)
print(s)

