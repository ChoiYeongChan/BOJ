import sys
a=int(sys.stdin.readline())
b=[]
for i in range(a):
    c,d=map(str,sys.stdin.readline().split())
    c=int(c)
    b.append((c,d))
b.sort(key=lambda x:x[0])
for i in b:
    print(i[0],i[1])