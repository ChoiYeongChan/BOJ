import sys
input=sys.stdin.readline
dp=[-1,-1,-1,1,-1,1,]
n=int(input())
for i in range(6,5001):
    a=dp[i-3]
    b=dp[i-5]
    if a==-1:
        if b==-1:
            dp.append(-1)
        else:
            dp.append(b+1)
    else:
        if b==-1:
            dp.append(a+1)
        else:
            dp.append(min(a,b)+1)
print(dp[n])