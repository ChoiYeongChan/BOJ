import sys
import itertools
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
result=0
p=itertools.permutations(a)
for i in p:
    s=0
    for j in range(len(i)-1):
        s+=abs(i[j]-i[j+1])
    if s>result:
        result=s
print(result)