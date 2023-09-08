from collections import deque

def solution(n, edge):
    answer = 0
    graph=[[]for _ in range(n+1)]
    visit=[0]*(n+1)
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    visit[1]=1
    q=deque([1])
    while q:
        x=q.popleft()
        for next in graph[x]:
            if not visit[next]:
                visit[next]=visit[x]+1
                q.append(next)
    max_v=max(visit)
    cnt=visit.count(max_v)
    if cnt>0:
        answer=cnt
    else:
        answer=1
    return answer