import sys
n=int(sys.stdin.readline())
conf=[]
for _ in range(n):
    conf.append(list(map(int,sys.stdin.readline().split())))
conf.sort(key=lambda x:(x[1],x[0]))
cnt=1
end=conf[0][1]
for i in range(1,n):
    if conf[i][0]>=end:
        cnt+=1
        end=conf[i][1]
print(cnt)