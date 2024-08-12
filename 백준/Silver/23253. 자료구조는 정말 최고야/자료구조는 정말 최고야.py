import sys
input=sys.stdin.readline
n,m=map(int,input().split())
flag=True
for _ in range(m):
    k=int(input())
    arr=list(map(int,input().split()))
    for j in range(k-1):
        if arr[j]<arr[j+1]:
            flag=False
            break
    if not flag:
        break
if flag:
    print('Yes')
else:
    print('No')