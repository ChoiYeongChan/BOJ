import sys
input=sys.stdin.readline
n,k=map(int,input().split())
arr=list(map(int,input().split()))
part=sum(arr[:k])
ans=part
for i in range(n-k):
    part+=(arr[i+k]-arr[i])
    ans=max(part,ans)
print(ans)