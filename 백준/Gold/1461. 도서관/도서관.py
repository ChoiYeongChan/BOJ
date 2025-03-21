import sys
input=sys.stdin.readline
n,m=map(int,input().split())
positive=[]
negative=[]
a=list(map(int,input().split()))
for i in a:
    if i>0:
        positive.append(i)
    else:
        negative.append(abs(i))
result=0
positive.sort(reverse=True)
negative.sort(reverse=True)
for i in range(0,len(positive),m):
    result+=positive[i]*2
for i in range(0,len(negative),m):
    result+=negative[i]*2
result-=max(abs(min(a)),max(a))
print(result)