import sys
input=sys.stdin.readline
a=[]
for _ in range(3):
    a.append(list(map(int,input().split())))
s=((a[1][0]-a[0][0])*(a[2][1]-a[0][1])-(a[1][1]-a[0][1])*(a[2][0]-a[0][0]))
if s>0:
    print(1)
elif s==0:
    print(0)
else:
    print(-1)