import sys
a,b=map(int,sys.stdin.readline().split())
x=set()
y=set()
for _ in range(a):
    x.add(sys.stdin.readline().rstrip())
for _ in range(b):
    y.add(sys.stdin.readline().rstrip())
z=list(x&y)
z.sort()
print(len(z))
for i in z:
    print(i)