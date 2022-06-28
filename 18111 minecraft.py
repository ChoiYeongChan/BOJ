import sys
a,b,c=map(int,sys.stdin.readline().split())
stack=[]
for i in range(a):
    stack.append(list(map(int,sys.stdin.readline().split())))
#print(m,n)
x=10000000000000000000
y=0
for k in range(257):
    max=0
    min=0
    for i in range(a):
        for j in range(b):
            if stack[i][j] <k:
                min+=k-stack[i][j]
            else:
                max+=stack[i][j]-k
    z=max+c
    if z<min:
        continue
    time=2*max + min
    if time<=x:
        x=time
        y=k
print(x,y)