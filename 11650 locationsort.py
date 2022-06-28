import sys
a=int(sys.stdin.readline())
b=[]
for i in range(a):
    b.append(list(map(int,sys.stdin.readline().split())))
b=sorted(b,key=lambda x:(x[0],x[1]))
for i in range(a):
    print(b[i][0],b[i][1])