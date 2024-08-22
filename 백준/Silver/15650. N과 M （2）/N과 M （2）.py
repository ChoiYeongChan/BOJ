import sys
from itertools import combinations
n,m=map(int,input().split())
arr=[i for i in range(1,n+1)]
c=list(combinations(arr,m))
for i in c:
    print(*i)