import sys
input=sys.stdin.readline
a=input().rstrip()
cnt=0
for i in range(len(a)-1):
    if a[i]!=a[i+1]:
        cnt+=1
if cnt%2!=0:
    cnt+=1
print(int(cnt/2))