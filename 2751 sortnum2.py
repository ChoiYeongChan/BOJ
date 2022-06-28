import sys
a=int(sys.stdin.readline())
b=[]
for i in range(a):
    b.append(int(sys.stdin.readline()))
b=list(set(b))
b.sort()
for i in range(len(b)):
    print(b[i])