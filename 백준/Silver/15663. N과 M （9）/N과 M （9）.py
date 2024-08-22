import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
visited=[False]*n
out=[]
def dfs(depth,n,m):
    if depth==m:
        print(' '.join(map(str,out)))
        return
    overlap=0
    for i in range(n):
        if not visited[i] and overlap!=a[i]:
            visited[i]=True
            out.append(a[i])
            overlap=a[i]
            dfs(depth+1,n,m)
            visited[i]=False
            out.pop()

dfs(0,n,m)