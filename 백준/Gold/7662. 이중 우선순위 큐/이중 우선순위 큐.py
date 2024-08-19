import sys
import heapq
input=sys.stdin.readline
t=int(input())
for i in range(t):
    min_heap=[]
    max_heap=[]
    k=int(input())
    deleted=[True]*k
    for i in range(k):
        a,b=input().rstrip().split()
        n=int(b)
        if a=='I':
            heapq.heappush(min_heap,(n,i))
            heapq.heappush(max_heap,(-n,i))
            deleted[i]=False
        else:
            if n==1:
                while max_heap and deleted[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    deleted[max_heap[0][1]]=True
                    heapq.heappop(max_heap)
            else:
                while min_heap and deleted[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    deleted[min_heap[0][1]]=True
                    heapq.heappop(min_heap)
    while min_heap and deleted[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and deleted[max_heap[0][1]]:
        heapq.heappop(max_heap)
    if max_heap and min_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')