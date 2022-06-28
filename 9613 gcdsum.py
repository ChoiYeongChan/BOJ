import sys
import math
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    a=list(map(int,input().split()))
    s=0
    for i in range(1,len(a)):
        for j in range(i+1,len(a)):
            s+=math.gcd(a[i],a[j])
    print(s)