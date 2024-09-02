import sys
from collections import Counter
input=sys.stdin.readline
s=input().rstrip()
c=Counter(s)
cnt=0
ans=''
mid=''
for i,j in list(c.items()):
    if j%2==1:
        cnt+=1
        mid=i
        if cnt>=2:
            print("I'm Sorry Hansoo")
            exit(0)
for i,j in sorted(c.items()):
    ans+=(i*(j//2))
print(ans+mid+ans[::-1])