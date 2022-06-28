import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int, input().split()))

d=[1]*n
for i in range(1,n):
    s=[]
    for j in range(i):
        if a[i]<a[j]:
            s.append(d[j])
    if not s:
        continue
    else:
        d[i]+=max(s)
print(max(d))