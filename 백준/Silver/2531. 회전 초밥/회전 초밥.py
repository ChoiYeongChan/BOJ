import sys
input=sys.stdin.readline
n,d,k,c=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(int(input()))
arr=arr+arr[:k]
cnt=0
part=arr[:k]
for i in range(k,n+k):
    p=set(part)
    p.add(c)
    cnt=max(len(p),cnt)
    part.pop(0)
    part.append(arr[i])
print(cnt)