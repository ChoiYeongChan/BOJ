import sys
a,b=sys.stdin.readline().split()
c=list(map(int,sys.stdin.readline().split()))
c.sort()
sum=0
for i in range(len(c)-2):
    for j in range(i+1,len(c)-1):
        for k in range(j+1,len(c)):
            d=c[i]+c[j]+c[k]
            if d>int(b):
                break
            if d>sum and d<=int(b):
                sum=d
print(sum)