import sys
input=sys.stdin.readline
k=int(input())
a=[0 for _ in range(46)]
b=[0 for _ in range(46)]
a[0]=1
a[1]=0

b[0]=0
b[1]=1

for i in range(2,46):
    a[i]=a[i-1]+a[i-2]
    b[i]=b[i-1]+b[i-2]
print(a[k],b[k])