import sys
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
fruit=[0]*10
kind=0
start=0
end=0
ans=0
while end<n:
    if fruit[arr[end]]==0:
        kind+=1
    fruit[arr[end]]+=1
    end+=1
    while kind>2:
        fruit[arr[start]]-=1
        if fruit[arr[start]]==0:
            kind-=1
        start+=1
    ans=max(ans,end-start)
print(ans)