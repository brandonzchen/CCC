import sys
inputmonth = int(sys.stdin.readline())
inputday = int(sys.stdin.readline())
if inputmonth==2 and inputday==18:
    print("Special")
if inputmonth==2 and inputday<18:
    print("Before")
if inputmonth==2 and inputday>18:
    print("After")
if inputmonth>2:
    print("After")
if inputmonth<2:
    print("Before")
