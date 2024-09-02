import sys
input=sys.stdin.readline
n=int(input())
candy=[]
for _ in range(n):
    candy.append(list(input().rstrip()))
def count():
    max_cnt=1
    for i in range(n):
        cnt=1
        for j in range(1,n):
            if candy[i][j]==candy[i][j-1]:
                cnt+=1
            else:
                cnt=1
            max_cnt=max(cnt,max_cnt)
        cnt=1
        for j in range(1,n):
            if candy[j][i]==candy[j-1][i]:
                cnt+=1
            else:
                cnt=1
            max_cnt=max(cnt,max_cnt)
    return max_cnt

ans=0
for i in range(n):
    for j in range(n):
        if j+1<n:
            candy[i][j],candy[i][j+1]=candy[i][j+1],candy[i][j]
            cnt=count()
            ans=max(ans,cnt)
            candy[i][j],candy[i][j+1]=candy[i][j+1],candy[i][j]
        if i+1<n:
            candy[i][j],candy[i+1][j]=candy[i+1][j],candy[i][j]
            cnt=count()
            ans=max(ans,cnt)
            candy[i][j],candy[i+1][j]=candy[i+1][j],candy[i][j]

print(ans)