import sys
input=sys.stdin.readline
x=int(input())
n=int(input())
s=0
for _ in range(n):
    a=list(map(int,input().split()))
    s+=a[0]*a[1]
if s==x:
    print("Yes")
else:
    print("No")