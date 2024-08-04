import sys
import math
input=sys.stdin.readline
n=int(input())
x=math.factorial(n)
x=str(x)[::-1]
cnt=0
for i in x:
    if i=='0':
        cnt+=1
    else:
        print(cnt)
        break