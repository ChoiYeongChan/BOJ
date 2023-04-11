import sys
input=sys.stdin.readline
n,m=map(int,input().split())
pack=[]
piece=[]
for _ in range(m):
    a,b=map(int,input().split())
    pack.append(a)
    piece.append(b)
pa=min(pack)
pi=min(piece)
print(min((n//6)*pa+(n%6)*pi,((n//6)+1)*pa,n*pi))
