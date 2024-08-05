import sys
input=sys.stdin.readline
N,M=map(int,input().split())
board=[]
for _ in range(N):
    board.append(input())
res=[]
for i in range(N-7):
    for j in range(M-7):
        black=0
        white=0
        for a in range(i,i+8):
            for b in range(j,j+8):
                if (a+b)%2==0:
                    if board[a][b]=='B':
                        white+=1
                    else:
                        black+=1
                else:
                    if board[a][b]=='B':
                        black+=1
                    else:
                        white+=1
        res.append(black)
        res.append(white)
print(min(res))