import sys
a,b=map(int,sys.stdin.readline().split())
suma=1
sumb=1
for i in range(b):
    suma*=a
    sumb*=b
    a-=1
    b-=1
print(suma//sumb)