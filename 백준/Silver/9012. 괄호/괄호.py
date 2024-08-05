import sys
input=sys.stdin.readline
n=int(input())
for _ in range(n):
    s=input().rstrip()
    a=[]
    flag=True
    for i in s:
        if i=='(':
            a.append('(')
        elif i==')':
            if len(a)==0:
                flag=False
                break
            else:
                if a[-1]=='(':
                    a.pop()
                else:
                    flag=False
                    break
    if len(a)==0 and flag==True:
        print('YES')
    else:
        print('NO')