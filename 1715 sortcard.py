import sys
import heapq
input=sys.stdin.readline
n=int(input())
card=[]
for _ in range(n):
    heapq.heappush(card,int(input()))
if len(card)==1:
    print(0)
else:
    s=0
    while len(card)>1:
        a=heapq.heappop(card)
        b=heapq.heappop(card)
        s+=a+b
        heapq.heappush(card,a+b)
print(s)