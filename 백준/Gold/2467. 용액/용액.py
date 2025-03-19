import sys
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
x=0
y=n-1
ans=abs(arr[x]+arr[y])
ax=x
ay=y
while x<y:
    tmp=arr[x]+arr[y]
    if abs(tmp)<ans:
        ax=x
        ay=y
        ans=abs(tmp)
        if ans==0:
            break
    if tmp<0:
        x+=1
    else:
        y-=1
print(arr[ax],arr[ay])