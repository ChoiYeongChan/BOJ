import sys
t=int(sys.stdin.readline())
def num(m,n,x,y):
    while x<=m*n:
        if (x-y)%n==0:
            return x
        x+=m
    return -1
for _ in range(t):
    m,n,x,y=map(int,sys.stdin.readline().split())
    print(num(m,n,x,y))
    '''
    a=0
    b=0
    cnt=0
    while 1:
        if a<m:
            a+=1
        else:
            a=1
        if b<n:
            b+=1
        else:
            b=1
        cnt+=1
        if a==x and b==y:
            ans=cnt
            break
        if a==m and b==n:
            ans=-1
            break
    print(ans)
    '''