from collections import deque
import sys

a=int(sys.stdin.readline())
b=[]
queue=deque()
for i in range(a):
    b=list(sys.stdin.readline().split())
    if b[0]=='push':
        queue.append(int(b[1]))
    elif b[0]=='pop':
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
        print(queue[0])
    elif b[0]=='back':
        print(queue[-1])