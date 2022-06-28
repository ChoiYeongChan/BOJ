n,r,c=map(int,input().split())
ans=0
def sol(x,y,n):
    global ans
    if x==r and y==c:
        print(ans)
        exit(0)
    if n==1:
        ans+=1
        return
    if not (x<=r<x+n and y<=c<y+n):
        ans+=n*n
        return
    sol(x,y,n//2)
    sol(x,y+n//2,n//2)
    sol(x+n//2,y,n//2)
    sol(x+n//2,y+n//2,n//2)
sol(0,0,2**n)
print(ans)
'''
s=[[0]*2**n for _ in range(2**n)]
def sol(x,y,n):
    global cnt
    if n>2:
        sol(x,y,n//2)
        sol(x,y+n//2,n//2)
        sol(x+n//2,y,n//2)        
        sol(x+n//2,y+n//2,n//2)
    else:
        s[x][y]=cnt
        s[x][y+1]=cnt+1
        s[x+1][y]=cnt+2
        s[x+1][y+1]=cnt+3
        cnt+=4
        return
cnt=0
sol(0,0,2**n)
print(s[r][c])
'''