import sys
a=int(sys.stdin.readline())
b=[]
for i in range(a):
    c=int(sys.stdin.readline())
    if c==0:
        b.pop()
    else:
        b.append(c)
print(sum(b))