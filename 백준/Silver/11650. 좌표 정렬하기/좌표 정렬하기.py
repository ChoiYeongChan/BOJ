import sys
input=sys.stdin.readline
n=int(input())
cord=[]
for _ in range(n):
    cord.append(list(map(int,input().split())))
cord.sort(key=lambda x:(x[0],x[1]))
for i in cord:
    print(i[0],i[1])