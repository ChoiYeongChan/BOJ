import sys
a=int(sys.stdin.readline())
b=[]
f=[0]*a
for i in range(a):
    b.append(list(map(int,sys.stdin.readline().split())))
for i in b:
    rank=1
    for j in b:
        if i[0]<j[0] and i[1]<j[1]:
            rank+=1
    print(rank,end=' ')