import sys
input=sys.stdin.readline
n=int(input())
for _ in range(n):
    left=[]
    right=[]
    a=input().rstrip()
    for i in a:
        if i=='>':
            if right:
                left.append(right.pop())
        elif i=='<':
            if left:
                right.append(left.pop())
        elif i=='-':
            if left:
                left.pop()
        else:
            left.append(i)
    left.extend(reversed(right))
    print(''.join(left))