import sys
while 1:
    a=list(sys.stdin.readline().rstrip())
    if a[0]=='0':
        break
    else:
        b=list(reversed(a))
        if a==b:
            print("yes")
        else:
            print("no")
