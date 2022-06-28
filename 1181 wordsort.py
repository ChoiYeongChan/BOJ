import sys
a=int(sys.stdin.readline())
b=[]
for i in range(a):
    b.append(sys.stdin.readline().rstrip())
b=list(set(b))
b.sort(key=lambda x:(len(x),x))
for i in range(len(b)):
    print(b[i])