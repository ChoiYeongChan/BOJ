import sys
input=sys.stdin.readline
n,l=map(int,input().split())
x=list(map(int,input().split()))
x.sort()
start=x[0]
end=x[0]+l
cnt=1
for i in range(n):
    if start<=x[i]<end:
        continue
    else:
        start=x[i]
        end=x[i]+l
        cnt+=1
print(cnt)