import sys
input=sys.stdin.readline
import heapq
n=int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
arr.sort()
h=[]
heapq.heappush(h,arr[0][1])
for i in range(1,len(arr)):
    if h[0]<=arr[i][0]:
        heapq.heappop(h)
        heapq.heappush(h,arr[i][1])
    else:
        heapq.heappush(h,arr[i][1])
print(len(h))
    