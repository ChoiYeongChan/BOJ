import sys
from itertools import combinations
input=sys.stdin.readline
card, target=map(int,input().split())
card_list=list(map(int,input().split()))
res=0
for c in combinations(card_list,3):
    tmp=sum(c)
    if res<tmp<=target:
        res=tmp
print(res)