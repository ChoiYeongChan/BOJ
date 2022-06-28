n=int(input())
dp=[[1,0],[0,1]]
for _ in range(n):
    x=int(input())
    if len(dp)>x:
        print(dp[x][0],dp[x][1])
    else:
        for i in range(len(dp),x+1):
            a=dp[i-1][0]+dp[i-2][0]
            b=dp[i-1][1]+dp[i-2][1]
            dp.append([a,b])
        print(dp[x][0],dp[x][1])