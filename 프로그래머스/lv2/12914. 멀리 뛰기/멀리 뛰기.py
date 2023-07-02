def solution(n):
    dp=[[0] for _ in range(2005)]
    dp[1]=1
    dp[2]=2
    for i in range(3, 2000):
        dp[i]=dp[i-1]+dp[i-2]
    
    answer = dp[n]%1234567
    return answer