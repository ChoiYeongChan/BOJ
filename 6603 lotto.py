import sys
from itertools import combinations
while 1:
    a=list(map(int,sys.stdin.readline().split()))
    if a[0]==0:
        break
    else:
        b=[]
        for i in range(1,a[0]+1):
            b.append(a[i])
        c=list(combinations(b,6))
        for i in c:
            for j in i:
                print(j,end=' ')
            print()
        print()