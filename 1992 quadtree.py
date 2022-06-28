import sys

def sol(x,y,n):
    a=matrix[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if a!=matrix[i][j]:
                a=-1
                break
    if a==-1:
        print("(",end='')
        n=n//2
        sol(x,y,n)
        sol(x,y+n,n)
        sol(x+n,y,n)
        sol(x+n,y+n,n)
        print(")",end='')
    elif a=='1':
        print(1,end='')
    else:
        print(0,end='')
n=int(sys.stdin.readline())
matrix=[[] for _ in range(n)]
for i in range(n):
    matrix[i]=list(sys.stdin.readline().rstrip())
sol(0,0,n)