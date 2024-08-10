import sys
a=set()
n=int(sys.stdin.readline())
s=[]
for i in range(n):
    s=list(sys.stdin.readline().split())
    if s[0]=='add':
        a.add(int(s[1]))
    elif s[0]=='check':
        if int(s[1]) in a:
            print('1')
        else:
            print('0')
    elif s[0]=='remove':
        a.discard(int(s[1]))
    elif s[0]=='toggle':
        if int(s[1]) in a:
            a.remove(int(s[1]))
        else:
            a.add(int(s[1]))
    elif s[0]=='all':
        a={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    elif s[0]=='empty':
        a.clear()