import sys
input=sys.stdin.readline
cnt=0
n=int(input())
a=666
while 1:
    if '666' in str(a):
        cnt+=1
    if cnt==n:
        print(a)
        break
    a+=1