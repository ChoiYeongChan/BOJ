import sys
a=list(sys.stdin.readline().rstrip().split('-'))
b=list(map(int,a[0].split('+')))
x=sum(b)
for i in range(1,len(a)):
    b=list(map(int,a[i].split('+')))
    x-=sum(b)
print(x)