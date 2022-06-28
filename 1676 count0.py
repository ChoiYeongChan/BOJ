n=int(input())
sum=1
while 1:
    if n==0:
        break
    else:
        sum*=n
        n-=1
b=list(map(int,str(sum)))
b.reverse()
cnt=0
for i in range(len(b)):
    if b[i]==0:
        cnt+=1
    else:
        break
print(cnt)