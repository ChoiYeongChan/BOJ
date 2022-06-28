import sys
a,b=map(int,sys.stdin.readline().split())
c=[]
for i in range(a):
    c.append(int(sys.stdin.readline()))
start=0
end=min(c)
while start<=end:
    mid=(start+end)//2
    cnt=0
    for i in c:
        cnt+=(i//mid)
    if cnt>=b:
        start=mid+1
    else:
        end=mid-1
print(end)
