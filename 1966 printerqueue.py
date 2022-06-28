import sys
a=int(sys.stdin.readline())
for i in range(a):
    cnt=0
    b,c=map(int,sys.stdin.readline().split())
    f=list(map(int,sys.stdin.readline().split()))
    g=[]
    for j in range(b):
        g.append((f[j],j))
    while 1:
        x=f.index(max(f))
        cnt+=1
        if g[x][1]==c:
            print(cnt)
            break
        else:
            g.pop(x)
            f.pop(x)
            for i in range(0,x):
                g.append(g.pop(0))
                f.append(f.pop(0))