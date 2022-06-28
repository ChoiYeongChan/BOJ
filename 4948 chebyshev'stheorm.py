x=123456*2+1
a=[True]*x
for i in range(2,int(x**0.5)+1):
    if a[i]:
        for j in range(2*i,x,i):
            a[j]=False

while(1):
    n=int(input())
    if n==0:
        break
    else:
        cnt=0
        for i in range(n+1,2*n+1):
            if a[i]:
                cnt+=1
        print(cnt)