import sys
room=[[i for i in range(15)]for _ in range(15)]
for i in range(1,15):
    for j in range(1,15):
        room[i][j]=room[i-1][j]+room[i][j-1]
T=int(input())
for _ in range(T):
    k=int(input())
    n=int(input())
    print(room[k][n])