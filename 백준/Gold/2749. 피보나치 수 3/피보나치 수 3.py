import sys
input=sys.stdin.readline
n=int(input())
#k=10**n, p=15*10**(n-1)
k=10**6
p=15*10**5
n%=p
a,b=0,1
for i in range(n-1):
    a,b=b%k,(a+b)%k
print(b)