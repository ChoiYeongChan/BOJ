import sys
input=sys.stdin.readline
n=int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
arr.sort(key=lambda x: (x[1],x[0]))
cnt=0
end=0
for x,y in arr:
    if end<=x:
        cnt+=1
        end=y
print(cnt)