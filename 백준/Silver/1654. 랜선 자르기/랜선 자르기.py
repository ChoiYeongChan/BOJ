import sys
input=sys.stdin.readline
k,n=map(int,input().split())
lan=[]
for _ in range(k):
    lan.append(int(input()))
start=1
end=max(lan)
while start<=end:
    mid=(start+end)//2
    cnt=0
    for i in lan:
        cnt+=i//mid
    if cnt>=n: # 개수가 많으면 더 길게 잘라야함
        start=mid+1
    else:
        end=mid-1
print(end)