import sys
input=sys.stdin.readline
n=int(input())
coord=[]
for _ in range(n):
    coord.append(list(map(int,input().split())))
coord.append(coord[0])
x=0
y=0
for i in range(n):
    x+=coord[i][0]*coord[i+1][1]
for i in range(n):
    y+=coord[i][1]*coord[i+1][0]
a=abs(round((x-y)/2,1))
print(a)