import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=set()
for _ in range(n):
    a.add(input().rstrip())
b=set()
for _ in range(m):
    b.add(input().rstrip())
res=sorted(list(a&b))
print(len(res))
for i in res:
    print(i)