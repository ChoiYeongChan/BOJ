import sys
n,m=map(int,sys.stdin.readline().split())

def twocount(n):
    a=0
    while n!=0:
        n=n//2
        a+=n
    return a

def fivecount(n):
    b=0
    while n!=0:
        n=n//5
        b+=n
    return b

print(min(twocount(n)-twocount(n-m)-twocount(m),fivecount(n)-fivecount(n-m)-fivecount(m)))