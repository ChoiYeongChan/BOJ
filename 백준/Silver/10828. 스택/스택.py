import sys
input=sys.stdin.readline
n=int(input())
stack=[]
for _ in range(n):
    s=list(input().split())
    if len(s)==1:
        if s[0]=='pop':
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif s[0]=='size':
            print(len(stack))
        elif s[0]=='empty':
            if stack:
                print(0)
            else:
                print(1)
        else:
            if stack:
                print(stack[-1])
            else:
                print(-1)
    else:
        stack.append(int(s[1]))