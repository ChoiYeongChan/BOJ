import sys
from collections import deque
input=sys.stdin.readline
a=deque([])
n=int(input())
for _ in range(n):
    s=list(input().split())
    if len(s)==1:
        if s[0]=='pop':
            if a:
                print(a.pop())
            else:
                print(-1)
        elif s[0]=='size':
            print(len(a))
        elif s[0]=='empty':
            if a:
                print(0)
            else:
                print(1)
        elif s[0]=='front':
            if a:
                print(a[-1])
            else:
                print(-1)
        else:
            if a:
                print(a[0])
            else:
                print(-1)
    else:
        a.appendleft(int(s[1]))