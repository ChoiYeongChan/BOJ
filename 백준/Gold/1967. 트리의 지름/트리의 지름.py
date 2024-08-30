import sys
input=sys.stdin.readline
n=int(input())
tree=[[]for _ in range(n+1)]
for _ in range(n-1):
    p,c,w=map(int,input().split())
    tree[p].append((c,w))
    tree[c].append((p,w))
def dfs(start):
    max=0
    idx=0
    visited=[False]*(n+1)
    visited[start]=True
    arr=[(start,0)]
    while arr:
        a=arr.pop()
        if a[1]>max:
            max=a[1]
            idx=a[0]
        visited[a[0]]=True
        for x in tree[a[0]]:
            if not visited[x[0]]:
                arr.append((x[0],x[1]+a[1]))
    return idx,max
i,_=dfs(1)
_,ans=dfs(i)
print(ans)