import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    dic={}
    n=int(input())
    for _ in range(n):
        a,b=input().rstrip().split()
        if b in dic:
            dic[b].append(a)
        else:
            dic[b]=[a]
    cnt=1
    for x in dic:
        cnt*=len(dic[x])+1
    print(cnt-1)