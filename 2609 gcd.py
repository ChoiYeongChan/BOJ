def GCD(x,y):
    while(y):
        x,y=y,x%y
    return x
import sys
a,b=map(int,sys.stdin.readline().split())
c=GCD(a,b)
lcm=a*b//c
print(c)
print(lcm)