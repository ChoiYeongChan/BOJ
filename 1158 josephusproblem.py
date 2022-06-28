import sys
n,k=map(int,sys.stdin.readline().split())
a=[i for i in range(1,n+1)]
ans=[]
num=k-1
for i in range(n):
    if len(a)>num:
        ans.append(a.pop(num))
        num+=k-1
    elif len(a)<=num:
        num=num%len(a)
        ans.append(a.pop(num))
        num+=k-1
print("<",", ".join(str(i) for i in ans),">",sep='')