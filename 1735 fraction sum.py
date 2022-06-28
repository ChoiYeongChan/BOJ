import sys
import math
input=sys.stdin.readline
a,b=map(int,input().split())
c,d=map(int,input().split())
x=a*d+b*c
y=b*d
g=math.gcd(x,y)
print(x//g,y//g)