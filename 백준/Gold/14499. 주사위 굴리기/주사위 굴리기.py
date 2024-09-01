import sys
input=sys.stdin.readline
n,m,y,x,k=map(int,input().split())
graph=[]
dx=[0,1,-1,0,0]
dy=[0,0,0,-1,1]
dice=[0,0,0,0,0,0]
for _ in range(n):
    graph.append(list(map(int,input().split())))
command=list(map(int,input().split()))
def roll(n):
    if n==1:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]=dice[3],dice[1],dice[0],dice[5],dice[4],dice[2]
    elif n==2:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]=dice[2],dice[1],dice[5],dice[0],dice[4],dice[3]
    elif n==3:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]=dice[4],dice[0],dice[2],dice[3],dice[5],dice[1]
    else:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]=dice[1],dice[5],dice[2],dice[3],dice[0],dice[4]
for i in command:
    if 0<=x+dx[i]<m and 0<=y+dy[i]<n:
        y+=dy[i]
        x+=dx[i]
        roll(i)
        if graph[y][x]==0:
            graph[y][x]=dice[5]
        else:
            dice[5]=graph[y][x]
            graph[y][x]=0
        print(dice[0])