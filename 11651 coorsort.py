import sys
a=int(sys.stdin.readline())
b=[]
for i in range(a):
    c,d=map(int,sys.stdin.readline().split())
    b.append((c,d))
b.sort(key=lambda x: (x[1],x[0]))
for i in b:
    print(i[0],i[1])