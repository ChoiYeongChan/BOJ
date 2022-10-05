import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=set()
for _ in range(n):
    a.add(input().rstrip())
cnt=0
for _ in range(m):
    if input().rstrip() in a:
        cnt+=1
print(cnt)