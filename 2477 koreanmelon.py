import sys
input=sys.stdin.readline
n=int(input())
w=0
h=0
wi=0
hi=0
a=[0]*6
for i in range(6):
    a[i]=list(map(int,input().split()))
    if a[i][0]>2:
        if h<a[i][1]:
            h=a[i][1]
            hi=i
    else:
        if w<a[i][1]:
            w=a[i][1]
            wi=i
subw=abs(a[(wi-1)%6][1]-a[(wi+1)%6][1])
subh=abs(a[(hi-1)%6][1]-a[(hi+1)%6][1])
print((w*h-subw*subh)*n)