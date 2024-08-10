import sys
input=sys.stdin.readline
dp=[0,1,2,4]
for i in range(8):
    dp.append(dp[i+1]+dp[i+2]+dp[i+3])
n=int(input())
for _ in range(n):
    x=int(input())
    print(dp[x])