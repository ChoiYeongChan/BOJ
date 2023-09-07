import heapq
def solution(operations):
    heap=[]
    for i in operations:
        op, n= i.split(" ")
        if op=="I":
            heapq.heappush(heap,int(n))
        if i=="D -1" and heap:
            heapq.heappop(heap)
        if i=="D 1" and heap:
            heap=list(heap)
            heap.sort()
            heap.pop()
            heapq.heapify(heap)
    list(heap)
    if len(heap)>1:
        heap.sort()
        ma=heap[-1]
        mi=heap[0]
        return [ma,mi]
    elif len(heap)==1:
        return [heap[0],heap[0]]
    else:
        return [0,0]