def pointfind(initial):
    result=0
    if initial==0:
        result=3
    if initial==3:
        result=0
    if initial==1:
        result=1
    return result


a=[0,1,3]
x=0
s=0
p=[]
g1=[]
g2=[]
g3=[]
g4=[]
p.append(g1)
p.append(g2)
p.append(g3)
p.append(g4)
for i in range(3):
    for j in range(3):
        for k in range (3):
            for l in range(3):
                for m in range(3):
                    for n in range(3):
                        f=[a[i],a[j],a[k],a[l],a[m],a[n]]
                        g1.append(0)
                        g1.append(f[0])
                        g1.append(f[1])
                        g1.append(f[2])
                        total1=sum(g1)

                        g2.append(pointfind(f[0]))
                        g2.append(0)
                        g2.append(f[3])
                        g2.append(f[4])
                        total2=sum(g2)

                        g3.append(pointfind(f[1]))
                        g3.append(pointfind(f[3]))
                        g3.append(0)
                        g3.append(f[5])
                        total3=sum(g3)

                        g4.append(pointfind(f[2]))
                        g4.append(pointfind(f[4]))
                        g4.append(pointfind(f[5]))
                        g4.append(0)
                        total4=sum(g4)
                        

                        
                        
                        if total1 == total2 and total1 == total3 and total1 == total4:
                            x+=1
                            print(p)
                        
                        

                        g1.clear()
                        g2.clear()
                        g3.clear()
                        g4.clear()
print(x)

          
          
                
                        




                        
    

