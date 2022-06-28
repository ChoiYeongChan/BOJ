import sys
n=int(sys.stdin.readline())
a=[]
for _ in range(n):
    t,p=map(int,sys.stdin.readline().split())
    a.append([t,p])
dp=[0 for i in range(n+1)]
for i in range(n-1,-1,-1):
    if i + a[i][0]>n:
        dp[i]=dp[i+1]
    else:
        dp[i]=max(a[i][1]+dp[i+a[i][0]],dp[i+1])
print(dp[0])