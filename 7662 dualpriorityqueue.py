import sys
import heapq
result=[]
t=int(sys.stdin.readline())
for _ in range(t):
    visited=[False]*1000001
    minH,maxH=[],[]
    k=int(sys.stdin.readline())
    for i in range(k):
        s=list(sys.stdin.readline().rstrip().split())
        if s[0]=='I':
            heapq.heappush(minH,(int(s[1]),i))
            heapq.heappush(maxH,(-int(s[1]),i))
            visited[i]=True
        else:
            if s[1]=='1':
                while maxH and not visited[maxH[0][1]]:
                    heapq.heappop(maxH)
                if maxH:
                    visited[maxH[0][1]]=False
                    heapq.heappop(maxH)
            else:
                while minH and not visited[minH[0][1]]:
                    heapq.heappop(minH)
                if minH:
                    visited[minH[0][1]]=False
                    heapq.heappop(minH)
    while minH and not visited[minH[0][1]]:
        heapq.heappop(minH)
    while maxH and not visited[maxH[0][1]]:
        heapq.heappop(maxH)
    if minH and maxH:
        print(-maxH[0][0],minH[0][0])
    else:
        print("EMPTY")