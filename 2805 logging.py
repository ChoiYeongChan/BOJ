import sys
a,b=map(int,sys.stdin.readline().split())
c=list(map(int,sys.stdin.readline().split()))
start=0
end=max(c)
while start<=end:
    mid=(start+end)//2
    m=0
    for i in c:
        if i-mid>0:
           m+=i-mid
        if m>b:
            break
    if m>=b:
        start=mid+1
    else:
        end=mid-1
print(end)