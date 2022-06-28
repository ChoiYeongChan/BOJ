import sys
a,b=map(int,sys.stdin.readline().split())
c=[]
for i in range(a):
    c.append((sys.stdin.readline().rstrip(),i+1))
f=sorted(c,key=lambda x:x[0])
for i in range(b):
    d=sys.stdin.readline().rstrip()
    if ord(d[0])<58:
        print(c[int(d)-1][0])
    else:
        start=0
        end=len(c)-1
        while start<=end:
            mid=(start+end)//2
            if f[mid][0]>d:
                end=mid-1
            else:
                start=mid+1
        print(f[end][1])