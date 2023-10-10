import sys
input=sys.stdin.readline
ans=-2**31-1
def calc(num1,op,num2):
    if op=='+':
        return num1+num2
    elif op=='-':
        return num1-num2
    elif op=='*':
        return num1*num2
def dfs(idx, target):
    global ans
    if idx==N-1:
        ans=max(ans,target)
        return
    if idx+2<N:
        dfs(idx+2,calc(target,data[idx+1],data[idx+2]))
    if idx+4<N:
        dfs(idx+4,calc(target,data[idx+1],calc(data[idx+2],data[idx+3],data[idx+4])))
N=int(input())
data=list(input().rstrip())
for i in range(N):
    if i%2==0:
        data[i]=int(data[i])
target=data[0]
dfs(0,target)
print(ans)