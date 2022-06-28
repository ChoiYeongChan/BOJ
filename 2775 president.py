import sys
a=int(sys.stdin.readline())
b=[]
b.append(list(range(0,15)))
for j in range(1,15):
    b.append([0])
    for l in range(1,15):            
        x=b[j-1][l]+b[j][l-1]
        b[j].append(x)
for i in range(a):
    k=int(sys.stdin.readline())
    n=int(sys.stdin.readline())
    print(b[k][n])