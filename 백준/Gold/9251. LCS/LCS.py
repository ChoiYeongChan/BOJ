import sys
input=sys.stdin.readline
s1=input().rstrip()
s2=input().rstrip()
l1=len(s1)
l2=len(s2)
dp=[[0]*(l2+1) for _ in range(l1+1)]
for i in range(1,l1+1):
    for j in range(1,l2+1):
        if s1[i-1]==s2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i][j-1],dp[i-1][j])
print(dp[-1][-1])