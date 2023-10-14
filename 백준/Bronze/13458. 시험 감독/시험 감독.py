import math
N=int(input())
A=list(map(int,input().split()))
B,C=map(int,input().split())
cnt=0
for i in A:
    i-=B
    cnt+=1
    if i>0:
        cnt=cnt+math.ceil(i/C)
print(cnt)