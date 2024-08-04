import sys
input=sys.stdin.readline
n=int(input())
num=list(map(int,input().split()))
m=max(num)
new=[]
for i in num:
    new.append(i/m*100)
print(sum(new)/n)