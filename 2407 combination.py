import sys
import math
n,m=map(int,sys.stdin.readline().split())
x=math.factorial(n)
y=(math.factorial(n-m))*(math.factorial(m))
print(x//y)