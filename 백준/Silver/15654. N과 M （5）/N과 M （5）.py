import sys
from itertools import permutations
input=sys.stdin.readline
n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
c=list(permutations(arr,m))
for i in c:
    print(*i)