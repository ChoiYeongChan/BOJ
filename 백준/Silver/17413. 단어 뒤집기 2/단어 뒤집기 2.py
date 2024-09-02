import sys
input=sys.stdin.readline
stack=[]
ans=''
flag=False
s=input().rstrip()+' '
for i in s:
    if i=='<':
        flag=True
        for _ in range(len(stack)):
            ans+=stack.pop()
    stack.append(i)
    if i=='>':
        flag=False
        for _ in range(len(stack)):
            ans+=stack.pop(0)
    if i==' ' and not flag:
        stack.pop()
        for _ in range(len(stack)):
            ans+=stack.pop()
        ans+=' '
print(ans)