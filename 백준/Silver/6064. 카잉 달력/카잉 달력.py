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