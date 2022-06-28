import sys
t=int(sys.stdin.readline())
for _ in range(t):
    p=sys.stdin.readline().rstrip()
    p=p.replace('RR','')
    n=int(sys.stdin.readline())
    x=list(sys.stdin.readline().rstrip()[1:-1].split(','))
    r=0
    f=0
    b=0

    for i in p:
        if i=='R':
            r+=1
        else:
            if r%2==0:
                f+=1
            else:
                b+=1
    if f+b<=n:
        x=x[f:n-b]
        if r%2==1:
            print('['+','.join(x[::-1])+']')
        else:
            print('['+','.join(x)+']')
    else:
        print('errpr')