import sys
n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
s=list(sys.stdin.readline().rstrip())
cnt=0
ans=0
stack=[]
for i in range(m):
    if s[i]=='O':
        continue
    else:
        stack.append(i)
for i in range(1,len(stack)):
    if stack[i]-stack[i-1]==2:
        cnt+=1
    else:
        cnt=0
    if cnt>=n:
        ans+=1
print(ans)
'''
x=1+2*n
p='I'+'OI'*n
cnt=0
for i in range(m-x+1):
    y=''
    for j in range(x):
        y+=s[i+j]
    if y==p:
        cnt+=1
print(cnt)

'''