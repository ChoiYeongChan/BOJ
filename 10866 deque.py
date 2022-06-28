from collections import deque
import sys
a=int(sys.stdin.readline())
b=[]
queue=deque()
for i in range(a):
    b=list(sys.stdin.readline().split())
    if b[0]=='push_front':
        queue.appendleft(int(b[1]))
    elif b[0]=='push_back':
        queue.append(int(b[1]))
    elif b[0]=='pop_front':
        if len(queue)==0:
            print('-1')
        else:
            print(queue.popleft())
    elif b[0]=='pop_back':
        if len(queue)==0:
            print('-1')
        else:
            print(queue.pop())
    elif b[0]=='size':
        print(len(queue))
    elif b[0]=='empty':
        if len(queue)==0:
            print('1')
        else:
            print('0')
    elif b[0]=='front':
        if len(queue)==0:
            print('-1')
        else:
            print(queue[0])
    elif b[0]=='back':
        if len(queue)==0:
            print('-1')
        else:
            print(queue[-1])