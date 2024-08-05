import sys
import bisect
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
a.sort()
m=int(input())
b=list(map(int,input().split()))
for i in b:
    if a[bisect.bisect(a,i)-1]==i:
        print(1)
    else:
        print(0)