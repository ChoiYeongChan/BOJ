import sys
from itertools import permutations
from copy import deepcopy
input=sys.stdin.readline
N,M,K=map(int,input().split())
arr=[]
for _ in range(N):
    arr.append(list(map(int,input().split())))
rot=[]
for _ in range(K):
    rot.append(list(map(int,input().split())))
seq=[i for i in range(0,K)]
x=list(permutations(seq,K))
ans=100000
for i in x:
    arr2=deepcopy(arr)
    for j in range(K):
        r,c,s=rot[i[j]]
        r-=1
        c-=1
        for n in range(s,0,-1):
            tmp=arr2[r-n][c+n]
            arr2[r-n][c-n+1:c+n+1]=arr2[r-n][c-n:c+n]
            for m in range(r-n,r+n):
                arr2[m][c-n]=arr2[m+1][c-n]
            arr2[r+n][c-n:c+n]=arr2[r+n][c-n+1:c+n+1]
            for m in range(r+n,r-n,-1):
                arr2[m][c+n]=arr2[m-1][c+n]
            arr2[r-n+1][c+n]=tmp
    for x in arr2:
        ans=min(ans,sum(x))
print(ans)    