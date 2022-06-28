from itertools import combinations
import sys
n,s=map(int,sys.stdin.readline().split())
a=list(map(int,sys.stdin.readline().split()))
cnt=0
for i in range(1,n+1):
    c=combinations(a,i)
    for x in c:
        if sum(x)==s:
            cnt+=1
print(cnt)