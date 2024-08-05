import sys
input=sys.stdin.readline
while 1:
    s=input().rstrip()
    if s=='.':
        break
    else:
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
            elif i=='[':
                a.append('[')
            elif i==']':
                if len(a)==0:
                    flag=False
                    break
                else:
                    if a[-1]=='[':
                        a.pop()
                    else:
                        flag=False
                        break
        if len(a)==0 and flag==True:
            print('yes')
        else:
            print('no')