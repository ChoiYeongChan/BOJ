import sys
input=sys.stdin.readline
n=int(input())
for i in range(n):
    s = i+sum(map(int,str(i)))
    if s==n:
        print(i)
        break
else:
    print(0)