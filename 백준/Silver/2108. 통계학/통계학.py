import sys
from collections import Counter
input=sys.stdin.readline
n=int(input())
a=[]
for _ in range(n):
    a.append(int(input()))
a.sort()
print(round(sum(a)/n))
print(a[n//2])
x=Counter(a).most_common(2)
if len(x)>1:
    if x[0][1]==x[1][1]: #같다면 두번째 작은 값
        print(x[1][0])
    else:
        print(x[0][0])
else:
    print(x[0][0])
print(a[-1]-a[0])