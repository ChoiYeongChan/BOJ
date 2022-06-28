import sys
input=sys.stdin.readline
p=[0 for _ in range(10001)]
p[1]=1
for i in range(2,98):
    for j in range(i*2,10001,i):
        p[j]=1
n=int(input())
for _ in range(n):
    a=int(input())
    b=a//2
    for j in range(b,1,-1):
        if p[a-j]==0 and p[j]==0:
            print(j,a-j)
            break