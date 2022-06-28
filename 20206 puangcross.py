import sys
input=sys.stdin.readline
a,b,c=map(int,input().split())
x1,x2,y1,y2=map(int,input().split())
if a==0:
    y=(-1)*c/b
    if (y-y1)*(y-y2)<0:
        print('Poor')
    else:
        print('Lucky')
elif b==0:
    x=(-1)*c/a
    if (x-x1)*(x-x2)<0:
        print('Poor')
    else:
        print('Lucky')
else:
    if a*b<0:
        if((a*x2+b*y1+c)*(a*x1+b*y2+c)<0):
            print('Poor')
        else:
            print('Lucky')
    else:
        if((a*x1+b*y1+c)*(a*x2+b*y2+c)<0):
            print('Poor')
        else:
            print('Lucky')