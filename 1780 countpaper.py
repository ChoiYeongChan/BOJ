import sys
def sol(x,y,n):
    global a,b,c
    color=paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color!=paper[i][j]:
                sol(x,y,n//3)
                sol(x,y+n//3,n//3)
                sol(x,y+n//3*2,n//3)
                sol(x+n//3,y,n//3)
                sol(x+n//3,y+n//3,n//3)
                sol(x+n//3,y+n//3*2,n//3)
                sol(x+n//3*2,y,n//3)
                sol(x+n//3*2,y+n//3,n//3)
                sol(x+n//3*2,y+n//3*2,n//3)
                return
    if color==-1:
        a+=1
    elif color==0:
        b+=1
    else:
        c+=1
n=int(sys.stdin.readline())
paper=[]
for _ in range(n):
    paper.append(list(map(int,sys.stdin.readline().split())))
a,b,c=0,0,0
sol(0,0,n)
print(a)
print(b)
print(c)