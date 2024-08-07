import sys
import math
input=sys.stdin.readline
m,n=map(int,(input().split()))
for i in range(m,n+1):
    if i==1:
        continue
    a=int(math.sqrt(i))+1
    flag=True
    for j in range(2,a):
        if i%j==0:
            flag=False
            break
    if flag:
        print(i)