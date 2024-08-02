import sys
input=sys.stdin.readline
while(1):
    x=list(map(int,input().split()))
    c=max(x)
    x.remove(c)
    a=x[0]
    b=x[1]
    if a==0 and b==0 and c==0:
        break
    else:
        if a**2+b**2==c**2:
            print("right")
        else:
            print("wrong")