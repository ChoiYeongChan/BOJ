import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    cnt=1
    n=int(input())
    a=[]
    for _ in range(n):
        a.append(list(map(int,input().split())))
    a.sort()
    m=a[0][1]
    for i in range(1,n):
        if m>a[i][1]:
            cnt+=1
            m=a[i][1]
    print(cnt)