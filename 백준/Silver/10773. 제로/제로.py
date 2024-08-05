import sys
input=sys.stdin.readline
res=[]
k=int(input())
for _ in range(k):
    n=int(input())
    if n==0:
        res.pop()
    else:
        res.append(n)
print(sum(res))