from collections import deque
N=int(input())
def combinations(array,r):
    for i in range(len(array)):
        if r==1:
            yield [array[i]]
        else:
            for next in combinations(array[i+1:],r-1):
                yield [array[i]]+next
def is_connected(nodes):
    q=deque()
    check=[0 for _ in range(N)]
    q.append(nodes[0])
    check[nodes[0]]=1
    while q:
        node=q.popleft()
        for i in range(len(arr[node])):
            if arr[node][i]==0:
                continue
            if i not in nodes:
                continue
            if check[i]==0:
                check[i]=1
                q.append(i)
    return check.count(1)==len(nodes)
def get_total(nodes):
    total=0
    for node in nodes:
        total+=population[node]
    return total
population=list(map(int,input().split()))
arr=[[0 for _ in range(N)]for _ in range(N)]
for i in range(N):
    _,*dsts=map(int,input().split())
    for dst in dsts:
        arr[i][dst-1]=1


x={i for i in range(N)}
ans=987654321
for i in range(1,N//2+1):
    comb=combinations(list(x),i)
    for a in comb:
        b=list(x.difference(a))
        if is_connected(a) and is_connected(b):
            a_total=get_total(a)
            b_total=get_total(b)
            ans=min(ans,abs(a_total-b_total))
            
if ans==987654321:
    print(-1)
else:
    print(ans)