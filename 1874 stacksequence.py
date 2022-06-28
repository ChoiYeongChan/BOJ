import sys
a=int(sys.stdin.readline())
stack=[]
b=[]
cnt=1
x=True
for i in range(a):
    num=int(sys.stdin.readline())
    while cnt<=num:
        b.append(cnt)
        stack.append('+')
        cnt+=1
    if b[-1]==num:
        b.pop()
        stack.append('-')
    else:
        print("NO")
        x=False
        break
if x==True:
    for j in range(len(stack)):
        print(stack[j])