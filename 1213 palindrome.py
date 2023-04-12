import sys
from collections import Counter
input=sys.stdin.readline
s=list(map(str,input().rstrip()))
s.sort()
check=Counter(s)
cnt=0
mid=""
for i in check:
    if check[i]%2!=0:
        cnt+=1
        mid+=i
        s.remove(i)
    
    if cnt>1:
        break
if cnt>1:
    print("I'm Sorry Hansoo")
else:
    result=""
    for i in range(0,len(s),2):
        result+=s[i]
    print(result+mid+result[::-1])