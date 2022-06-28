import sys
while 1:
    a=list(sys.stdin.readline().rstrip())
    b=True
    c=[]
    if len(a)==1 and a[0]=='.':
        break
    else:
        for i in a:
            if i=='(':
                c.append(i)
            elif i==')':
                if len(c)==0 or c[-1]=='[':
                    b=False
                    break
                elif c[-1]=='(':
                    c.pop()
            elif i=='[':
                c.append(i)
            elif i==']':
                if len(c)==0 or c[-1]=='(':
                    b=False
                    break
                elif c[-1]=='[':
                    c.pop()
            else:
                continue
    if len(c)==0 and b==True:
        print('yes')
    else:
        print('no')
