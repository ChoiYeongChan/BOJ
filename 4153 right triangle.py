import sys
while 1:
    b,c,d=map(int,sys.stdin.readline().split())
    if b==0 and c==0 and d==0:
        break
    else:
        a=list((b,c,d))
        a.sort()
        if a[0]*a[0]+a[1]*a[1]==a[2]*a[2]:
            print("right")
        else:
            print("wrong")