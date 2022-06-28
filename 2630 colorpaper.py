import sys
def sol(x,y,n):
    global a,b
    color=paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color!=paper[i][j]:
                sol(x,y,n//2)
                sol(x,y+n//2,n//2)
                sol(x+n//2,y,n//2)
                sol(x+n//2,y+n//2,n//2)
                return
    if color==0:
        a+=1
    else:
        b+=1
    
n=int(sys.stdin.readline())
paper=[]
for _ in range(n):
    paper.append(list(map(int,sys.stdin.readline().split())))
a,b=0,0
sol(0,0,n)
print(a)
print(b)