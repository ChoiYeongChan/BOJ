n=int(input())
a=[0,1,2,4]
for i in range(4,11):
    a.append(a[i-1]+a[i-2]+a[i-3])
for _ in range(n):
    x=int(input())
    print(a[x])