import sys
input=sys.stdin.readline
n=int(input())
data=[[0]*n for _ in range(n)]
student=[]
for _ in range(n**2):
    student.append(list(map(int,input().split())))
dx=[0,0,-1,1]
dy=[1,-1,0,0]
for s in student:
    a=[]
    for x in range(n):
        for y in range(n):
            if data[x][y]==0:
                like,empty=0,0
                for k in range(4):
                    nx=x+dx[k]
                    ny=y+dy[k]
                    if 0<=nx<n and 0<=ny<n:
                        if data[nx][ny] in s[1:]:
                            like+=1
                        if data[nx][ny]==0:
                            empty+=1
                a.append((x,y,like,empty))
    a.sort(key=lambda x:(-x[2],-x[3],x[0],x[1]))
    data[a[0][0]][a[0][1]]=s[0]
ans=0
score=[0,1,10,100,1000]
student.sort()
for i in range(n):
    for j in range(n):
        cnt=0
        for k in range(4):
            nx=i+dx[k]
            ny=j+dy[k]
            if 0<=nx<n and 0<=ny<n:
                if data[nx][ny] in student[data[i][j]-1]:
                    cnt+=1
        ans+=score[cnt]
print(ans)