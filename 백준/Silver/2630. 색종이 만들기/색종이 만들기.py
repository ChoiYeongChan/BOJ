import sys
input=sys.stdin.readline
n=int(input())
paper=[]
result=[]
for _ in range(n):
    paper.append(list(map(int,input().split())))

def sol(x,y,n):
    color=paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if paper[i][j]!=color:
                sol(x, y, n//2)
                sol(x, y+n//2, n//2)
                sol(x+n//2, y, n//2)
                sol(x+n//2, y+n//2, n//2)
                return
    if color==0:
        result.append(0)
    else:
        result.append(1)
sol(0,0,n)
print(result.count(0))
print(result.count(1))