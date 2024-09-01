import sys
input=sys.stdin.readline
n=int(input())
s=[-1]+list(map(int,input().split()))
k=int(input())
def change(n):
    s[n]=1-s[n]
for _ in range(k):
    a,b=map(int,input().split())
    if a==1:
        for i in range(b,n+1,b):
            change(i)
    else:
        change(b)
        i=1
        while b-i>=1 and b+i<=n and s[b-i]==s[b+i]:
            change(b+i)
            change(b-i)
            i+=1
for i in range(1,n+1):
    print(s[i],end=" ")
    if i%20==0:
        print()