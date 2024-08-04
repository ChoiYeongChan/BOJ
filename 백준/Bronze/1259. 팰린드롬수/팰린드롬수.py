import sys
input=sys.stdin.readline
while 1:
    x=input().rstrip()
    if x=='0':
        break
    else:
        if x==x[::-1]:
            print("yes")
        else:
            print("no")