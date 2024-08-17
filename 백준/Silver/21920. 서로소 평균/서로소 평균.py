import sys
import math
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
x=int(input())
s=[]
for i in range(n):
    if a[i]!=x:
        if math.gcd(a[i],x)==1:
            s.append(a[i])
print('{:.6f}'.format(sum(s)/len(s)))