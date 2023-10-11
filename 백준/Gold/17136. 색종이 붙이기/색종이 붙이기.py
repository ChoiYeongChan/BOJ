import sys
input=sys.stdin.readline
sys.setrecursionlimit=(10**6)
paper=[]
for _ in range(10):
    paper.append(list(map(int,input().split())))
remain=[5,5,5,5,5]
cnt=25
def check(x,y,offset):
    for i in range(x,x+offset+1):
        for j in range(y,y+offset+1):
            if paper[i][j]!=1:
                return False
    return True

def backtracking(x,y,c):
    global remain,cnt
    if x>=10:
        cnt=min(cnt,c)
        return
    if y>=10:
        backtracking(x+1,0,c)
        return
    if paper[x][y]==1:
        for k in range(5):
            if remain[k]==0:
                continue
            if x+k>=10 or y+k>=10:
                continue
            if not check(x,y,k):
                break
            for i in range(x,x+k+1):
                for j in range(y,y+k+1):
                    paper[i][j]=0
            remain[k]-=1
            backtracking(x,y+k+1,c+1)
            remain[k]+=1
            for i in range(x,x+k+1):
                for j in range(y,y+k+1):
                    paper[i][j]=1
    else:
        backtracking(x,y+1,c)
backtracking(0,0,0)
if cnt==25:
    print(-1)
else:
    print(cnt)