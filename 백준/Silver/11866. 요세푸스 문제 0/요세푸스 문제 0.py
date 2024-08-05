import sys
from collections import deque
input=sys.stdin.readline
N,K=map(int,input().split())
arr=deque([])
for i in range(N):
    arr.append(i+1)
print('<',end='')
while arr:
    for _ in range(K-1):
        arr.append(arr.popleft())
    if len(arr)==1:
        print(arr.popleft(),end='>')
    else:
        print(arr.popleft(),end=', ')
    