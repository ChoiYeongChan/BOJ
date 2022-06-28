import sys
a=int(sys.stdin.readline())
for i in range(1,a+1):
    b=sum((map(int,str(i))))
    c=i+b
    if c==a:
        print(i)
        break
    if i==a:
        print(0)
    