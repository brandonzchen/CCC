from sys import argv

script, filename = argv
file = open(filename, "r")
humidity=int(file.readline())
time=int(file.readline())
t=0
for i in range(1,time):
    t=i
    if -6*t**4+humidity*t**3+2*t**2+t<=0:
        print("The balloon first touches ground at hour:")
        print(t)
        break
        exit()

print("The balloon does not touch the ground in the given time")
    
