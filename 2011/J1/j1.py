from sys import argv

script, filename = argv
file = open(filename, "r")
antennas=int(file.readline())
eyes=int(file.readline())
print("How many antennas?")
print("How many eyes?")
if antennas>=3 and eyes<=4:
    print("TroyMartian")
if antennas<=6 and eyes>=2:
    print("VladSaturnian")
if antennas<=2 and eyes<=3:
    print("GraemeMercurian")
