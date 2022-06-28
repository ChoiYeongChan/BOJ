import sys
a=int(sys.stdin.readline())
b=list(sys.stdin.readline().rstrip().split())
c=int(sys.stdin.readline())
d=list(sys.stdin.readline().rstrip().split())
e={}
for i in b:
    if int(i) in e:
        e[int(i)]+=1
    else :
        e[int(i)]=1
for i in d:
    if int(i) in e:
        print(e[int(i)],end=" ")
    else:
        print("0",end=" ")