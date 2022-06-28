import sys
n=int(sys.stdin.readline())
x=list(map(int,sys.stdin.readline().split()))
for i in range(n):
    x[i]=list([x[i],i])
x.sort()
m=x[0][0]
y=[x[0]]
for i in range(1,n):
    if x[i-1][0]<x[i][0]:
        y.append([y[i-1][0]+1,x[i][1]])
    else:
        y.append([y[i-1][0],x[i][1]])
y.sort(key=lambda x:x[1])
for i in range(n):
    print(y[i][0]-m,end=' ')