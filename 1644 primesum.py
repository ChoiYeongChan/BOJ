import sys
input=sys.stdin.readline
n=int(input())
a=[False,False]+[True]*(n-1)
prime=[]
for i in range(2,n+1):
    if a[i]:
        prime.append(i)
        for j in range(2*i,n+1,i):
            a[j]=False
ans=0
start=0
end=0
while end<=len(prime):
    temp=sum(prime[start:end])
    if temp==n:
        ans+=1
        end+=1
    elif temp<n:
        end+=1
    else:
        start+=1
print(ans)