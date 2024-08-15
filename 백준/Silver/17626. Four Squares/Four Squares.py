import sys
import math
input=sys.stdin.readline
n=int(input())
if math.isqrt(n)**2==n:
    print(1)
else:
    arr=[0]*(n+1)
    for i in range(math.isqrt(n)+1):
        arr[i**2]=1
    cnt=4
    for i in range(math.isqrt(n)+1):
        if arr[n-i**2]:
            cnt=2
            break
    if cnt==4:
        for i in range(math.isqrt(n)+1):
            for j in range(math.isqrt(n-i**2)+1):
                if arr[n-i**2-j**2]:
                    cnt=3
                    break
            if cnt==3:
                break
    print(cnt)