import sys
input=sys.stdin.readline
dp=[0]*1001
dp[1]=1
dp[2]=3
dp[3]=5
n=int(input())
for i in range(4,n+1):
    dp[i]=dp[i-2]*2+dp[i-1]
print(dp[n]%10007)