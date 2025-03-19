import sys
input=sys.stdin.readline
import heapq

n=int(input())
l=[]
for _ in range(n):
    l.append(list(map(int,input().split())))
l.sort(key=lambda x:x[1])
room=[]

heapq.heappush(room,l[0][2])
for i in range(1,n):
    if l[i][1]<room[0]:
        heapq.heappush(room,l[i][2])
    else:
        heapq.heappop(room)
        heapq.heappush(room,l[i][2])
print(len(room))
        