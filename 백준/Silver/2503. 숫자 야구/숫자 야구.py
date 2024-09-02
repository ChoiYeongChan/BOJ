import sys
input=sys.stdin.readline
from itertools import permutations
n=int(input())
nums=list(permutations(list(range(1,10)),3))
for _ in range(n):
    num,s,b=map(int,input().split())
    tmp=[]
    for i in nums:
        cnts=0
        cntb=0
        for j,snum in enumerate(str(num)):
            if int(snum)==i[j]:
                cnts+=1
            else:
                if int(snum) in i:
                    cntb+=1
        if s==cnts and b==cntb:
            tmp.append(i)
    nums=tmp
print(len(tmp))