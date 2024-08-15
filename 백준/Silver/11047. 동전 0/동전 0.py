import sys
input=sys.stdin.readline
n,k=map(int,input().split())
coin=[]
for _ in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)
cnt=0
for i in coin:
    if i<=k:
        if k%i==0:
            cnt+=k//i
            break
        else:
            a=k//i
            cnt+=a
            k-=a*i
print(cnt)