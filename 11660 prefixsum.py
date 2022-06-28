import sys
n,m=map(int,sys.stdin.readline().split())
a=[]
s=[[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(n):
    a.append(list(map(int,sys.stdin.readline().split())))
for i in range(n):
    for j in range(n):
        s[i+1][j+1]=s[i][j+1]+s[i+1][j]-s[i][j]+a[i][j]
for _ in range(m):
    x1,y1,x2,y2=map(int,sys.stdin.readline().split())
    print(s[x2][y2]-(s[x1-1][y2]+s[x2][y1-1]-s[x1-1][y1-1]))