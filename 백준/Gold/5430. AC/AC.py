import sys
from collections import deque
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    p=input().rstrip()
    n=int(input())
    arr=input().rstrip()[1:-1].split(",")
    queue=deque(arr)
    r=0
    flag=True
    if n==0:
        queue=[]
    for i in p:
        if i=='R':
            r+=1
        else:
            if not queue:
                flag=False
                print("error")
                break
            else:
                if r%2==0:
                    queue.popleft()
                else:
                    queue.pop()
    if flag:
        if r%2==0:
            print("["+",".join(queue)+"]")
        else:
            queue.reverse()
            print("["+",".join(queue)+"]")
    