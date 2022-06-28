import sys
import heapq
n=int(sys.stdin.readline())
heap=[]
for _ in range(n):
    num=int(sys.stdin.readline())
    if num!=0:
        heapq.heappush(heap,(-num,num))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)