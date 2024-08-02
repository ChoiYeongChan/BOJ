import sys
import math
input=sys.stdin.readline
n=int(input())
x=list(map(int,input().split()))
cnt=0
for i in x:
    flag=True
    if i==1:
        flag=False
    for j in range(2,i):
        if i%j==0:
            flag=False
            break
    if flag:
        cnt+=1
print(cnt)