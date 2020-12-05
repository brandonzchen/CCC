import sys
#
# input=sys.stdin.readline()
# x=input.split(":-(")
# y=input.split(":-)")
# if len(x)>len(y):
#     print("sad")
# if len(x)<len(y):
#     print("happy")
# if len(x)==len(y) and len(x)!=1:
#     print("unsure")
# if len(x)==len(y) and len(x)==1:
#     print("none")

# counthappy=0
# countsad=0
# input=sys.stdin.readline()
# x=list(input.strip())
# for i in range(len(x)-3):
#     if x[i]+x[i+1]+x[i+2]==":-)":
#         counthappy+=1
#     if x[i]+x[i+1]+x[i+2]==":-(":
#         countsad+=1
# if counthappy>countsad:
#     print("happy")
# elif counthappy<countsad:
#     print("sad")
# elif counthappy==countsad and counthappy!=0:
#     print("unsure")
# else:
#     print("none")

input=sys.stdin.readline()


happy=":-)"
sad=":-("
counthappy=input.count(happy)
countsad=input.count(sad)
if counthappy>countsad:
    print("happy")
elif counthappy<countsad:
    print("sad")
elif counthappy==countsad and counthappy!=0:
    print("unsure")
else:
    print("none")
