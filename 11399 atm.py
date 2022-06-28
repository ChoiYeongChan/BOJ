import sys
n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
a.sort()
dp=[0]*n
dp[0]=a[0]
for i in range(1,n):
    dp[i]=dp[i-1]+a[i]
print(sum(dp))