import sys
input=sys.stdin.readline
n,m,b=map(int,input().split())
height=[0]*257
for _ in range(n):
    for i in map(int,input().split()):
        height[i]+=1
    

ans=(1000000000)
h=0
for i in range(257):
    use=0
    take=0
    for j in range(257):
        if j<i:
            use+=(i-j)*height[j]
        else:
            take+=(j-i)*height[j]

    if take+b<use:
        continue
    cnt=take*2+use
    if cnt<=ans:
        ans=cnt
        h=i
print(ans,h)