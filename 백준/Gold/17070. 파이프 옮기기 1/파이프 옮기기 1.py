import sys
input=sys.stdin.readline
N=int(input())
board=[]
for i in range(N):
    board.append(list(map(int,input().split())))
dp=[[[0 for _ in range(N)]for _ in range(N)]for _ in range(3)]
dp[0][0][1]=1
for i in range(2,N):
    if board[0][i]==0:
        dp[0][0][i]=dp[0][0][i-1]
for i in range(1,N):
    for j in range(1,N):
        if board[i][j]==0:
            dp[0][i][j]=dp[0][i][j-1]+dp[1][i][j-1]
            dp[2][i][j]=dp[2][i-1][j]+dp[1][i-1][j]
        if board[i][j]==0 and board[i-1][j]==0 and board[i][j-1]==0:
            dp[1][i][j]=dp[0][i-1][j-1]+dp[1][i-1][j-1]+dp[2][i-1][j-1]
        
ans=0
for i in range(3):
    ans+=dp[i][N-1][N-1]
print(ans)