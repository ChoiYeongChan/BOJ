import sys
input=sys.stdin.readline
n=int(input())
stack=[]
ans=[]
cnt=1
flag=True
for _ in range(n):
    num=int(input())
    while cnt<=num:
        stack.append(cnt)
        cnt+=1
        ans.append('+')
    if stack[-1]==num:
        ans.append('-')
        stack.pop()
    else:
        flag=False
if flag:
    for i in ans:
        print(i)
else:
    print('NO')