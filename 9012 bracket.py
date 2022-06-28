import sys
a=int(sys.stdin.readline())
for i in range(a):
    b=list(sys.stdin.readline().rstrip())
    cnt=0
    for i in b:
        if i=='(':
            cnt+=1
        elif i==')':
            cnt-=1
        if cnt<0:
            break
    if cnt==0:
        print('YES')
    else:
        print('NO')
