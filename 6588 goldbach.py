import sys
input=sys.stdin.readline
p=[0 for _ in range(1000001)]
p[1]=1
for i in range(2,1001):
    for j in range(i*2,1000001,i):
        p[j]=1
while(1):
    a=int(input())
    if a==0:
        break
    b=a//2
    for j in range(b,1,-1):
        if p[a-j]==0 and p[j]==0:
            if a-j<j:
                print(a,"=",a-j,"+",j)
            else:
                print(a,"=",j,"+",a-j)
            break