import sys
from itertools import permutations
input=sys.stdin.readline
def permu(arr,n):
    res=[]
    if n==0:
        return [[]]
    for i, elem in enumerate(arr):
        for P in permu(arr[:i]+arr[i+1:],n-1):
            res+=[[elem]+P]
    return res
def sol(line_up):
    score=0
    now=0
    for i in inning:
        out=0
        b1,b2,b3=0,0,0
        while out<3:
            if i[line_up[now]]==0:
                out+=1
            elif i[line_up[now]]==1:
                score+=b3
                b1,b2,b3=1,b1,b2
            elif i[line_up[now]]==2:
                score+=(b2+b3)
                b1,b2,b3=0,1,b1
            elif i[line_up[now]]==3:
                score+=(b1+b2+b3)
                b1,b2,b3=0,0,1
            else:
                score+=(1+b1+b2+b3)
                b1,b2,b3=0,0,0
            now=(now+1)%9
    return score
N=int(input())
inning=[]
for _ in range(N):
    inning.append(list(map(int,input().split())))
ans=0
num=[1,2,3,4,5,6,7,8]
for line_up in permu(num,8):
    line_up=list(line_up[:3]+[0]+list(line_up[3:]))
    ans=max(ans,sol(line_up))
print(ans)