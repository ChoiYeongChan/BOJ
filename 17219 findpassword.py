import sys
a,b=map(int,sys.stdin.readline().split())
c={}
for _ in range(a):
    x,y=sys.stdin.readline().rstrip().split()
    c[x]=y
for _ in range(b):
    z=sys.stdin.readline().rstrip()
    print(c.get(z))