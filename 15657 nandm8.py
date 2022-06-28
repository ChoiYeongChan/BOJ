import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
ans=[]

def dfs(depth):
    if depth==m:
        print(' '.join(map(str,ans)))
        return
    for i in range(n):
        if depth == 0 or ans[depth - 1] <= a[i]:
            ans.append(a[i])
            dfs(depth + 1)
            ans.pop()
            
dfs(0)