

trout=int(sys.stdin.readline())
pike=int(sys.stdin.readline())
pikerel=int(sys.stdin.readline())
total=int(sys.stdin.readline())
count=0

for i in range(total//trout+1):
    for j in range(total//pike+1):
        for k in range(total//pikerel+1):
            if trout*i + pike*j + pikerel*k <= total and trout*i + pike*j + pikerel*k > 0:
                count+=1
                print(i, "Browwn Trout", j, "Pike", k, "Pikerel")

print(count)
