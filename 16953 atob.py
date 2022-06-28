import sys
a,b=map(int,sys.stdin.readline().split())
cnt=1
while(1):
    if a==b:
        break
    elif a>b or (b%2!=0 and b%10!=1):
        cnt=-1
        break
    else:
        if b%10==1:
            b=b//10
            cnt+=1
        else:
            b//=2
            cnt+=1
print(cnt)