import sys
input=sys.stdin.readline
n=int(input())
a=[]
d={}
num=[]
for _ in range(n):
    a.append(input().rstrip())
for i in range(n):
    for j in range(len(a[i])):
        if a[i][j] in d:
            d[a[i][j]]+=10**(len(a[i])-j-1)
        else:
            d[a[i][j]]=10**(len(a[i])-j-1)

for i in d.values():
    num.append(i)
num.sort(reverse=True)
sum=0
x=9
for i in num:
    sum+=x*i
    x-=1
print(sum)