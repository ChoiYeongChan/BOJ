import sys
s=list(sys.stdin.readline().rstrip())
bomb=list(sys.stdin.readline().rstrip())

stack=[]
for i in range(len(s)):
    stack.append(s[i])
    if stack[-1]==bomb[-1] and len(stack)>=len(bomb):
        if stack[-len(bomb):]==bomb:
            for i in range(len(bomb)):
                stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")