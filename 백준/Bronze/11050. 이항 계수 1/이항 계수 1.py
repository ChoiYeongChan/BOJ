import sys
from itertools import combinations
input=sys.stdin.readline
a,b=map(int,input().split())
l=[True]*a
print(len(list(combinations(l,b))))