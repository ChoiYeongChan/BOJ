import sys
input=sys.stdin.readline
dp=[0,1,1]
while 1:
    s=dp[-1]+dp[-2]
    if s>10**100:
        break
    else:
        dp.append(s)

while 1:
    a,b=map(int,input().split())
    if a==0 and b==0:
        break
    else:
        x=0
        y=0
        cnt=0
        for i in range(len(dp)+1):
            if a<dp[i]:
                x=i-1
                break
        for i in range(len(dp)+1):
            if b<dp[i]:
                y=i-1
                break
        print(y-x)