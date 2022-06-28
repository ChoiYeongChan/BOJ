import sys
n=int(sys.stdin.readline())
a=[]
s=[0]
for _ in range(n):
    a.append(list(map(int,sys.stdin.readline().split())))
k=2
for i in range(1,n):
    for j in range(k):
        if j==0:
            a[i][j]=a[i][j]+a[i-1][j]
        elif i==j:
            a[i][j]=a[i][j]+a[i-1][j-1]
        else:
            a[i][j]=a[i][j]+max(a[i-1][j-1],a[i-1][j])
    k+=1
print(max(a[n-1]))