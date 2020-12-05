from sys import argv

script, filename = argv
file = open(filename, "r")
word=(file.readline())

letters=['O','I','S','H','Z','X','N']

for i in range(len(word)-1):
    if word[i] in letters:
        pass
    else:
        print('NO')
        quit()
print('YES')

