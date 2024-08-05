import sys
input=sys.stdin.readline
n=int(input())
age=[]
for _ in range(n):
    a,b=map(str,input().split())
    a=int(a)
    age.append([a,b])
age.sort(key=lambda x:x[0])
for i in age:
    print(i[0],i[1])