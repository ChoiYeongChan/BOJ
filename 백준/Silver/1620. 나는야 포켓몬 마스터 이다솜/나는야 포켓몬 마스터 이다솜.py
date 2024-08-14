import sys
input=sys.stdin.readline
n,m=map(int,input().split())
dic={}
for i in range(n):
    x=input().rstrip()
    dic[x]=i+1
    dic[str(i+1)]=x
for _ in range(m):
    x=input().rstrip()
    print(dic[x])