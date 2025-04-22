import math
k,n=map(int,input().split())
l=[[0,0] for _ in range(2**k)]
lu=[[],[1]]
for i in range(1,k):
    for j in range(2**i):
        lu.append(lu[(2**i+j)//2]+[2**i+j])
for _ in range(n):
    c=input().split()
    if c[0]=='1':
        l[int(c[1])][0]+=int(c[2])
        s = int(math.log2(int(c[1])))
        for i in lu[int(c[1])]:
            l[i][1]+=int(c[2])*(2**(k-s)-1)
    else:
        s=int(math.log2(int(c[1])))
        z=0
        for i in lu[int(c[1])]:
            z+=l[i][0]
        z-=l[int(c[1])][0]
        z=z*(2**(k-s)-1)
        z+=l[int(c[1])][1]
        print(z)

