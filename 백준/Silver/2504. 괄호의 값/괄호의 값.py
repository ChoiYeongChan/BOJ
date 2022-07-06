import sys
input=sys.stdin.readline
a=list(input().rstrip())
stack=[]
ans=0
tmp=1
for i in range(len(a)):
    if a[i]=='(':
        stack.append(a[i])
        tmp*=2
    elif a[i]=='[':
        stack.append(a[i])
        tmp*=3
    elif a[i]==')':
        if not stack or stack[-1]=='[':
            ans=0
            break
        if a[i-1]=='(':
            ans+=tmp
        tmp//=2
        stack.pop()
    else:
        if not stack or stack[-1]=='(':
            ans=0
            break
        if a[i-1]=='[':
            ans+=tmp
        tmp//=3
        stack.pop()
if stack:
    ans=0
print(ans)