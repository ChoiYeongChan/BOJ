import sys
input=sys.stdin.readline
n=int(input())
nums=list(map(int,input().split()))
a,b,c,d=map(int,input().split())
maximum=sys.maxsize*-1
minimum=sys.maxsize
def sol(num,idx,a,b,c,d):
    global minimum,maximum
    if idx==n:
        maximum=max(maximum,num)
        minimum=min(minimum,num)
        return

    if a>0:
        sol(num+nums[idx],idx+1,a-1,b,c,d)
    if b>0:
        sol(num-nums[idx],idx+1,a,b-1,c,d)
    if c>0:
        sol(num*nums[idx],idx+1,a,b,c-1,d)
    if d>0:
        sol(int(num/nums[idx]),idx+1,a,b,c,d-1)

sol(nums[0],1,a,b,c,d)
print(maximum)
print(minimum)