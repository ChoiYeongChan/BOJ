import sys
input=sys.stdin.readline
n=int(input())
dic={}
a=list(map(int,input().split()))
for i in a:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
m=int(input())
b=list(map(int,input().split()))
for i in b:
    if i in dic:
        print(dic[i],end=' ')
    else:
        print(0,end=' ')