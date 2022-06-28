import sys
a,b,c,d=map(int,sys.stdin.readline().split())
e=[]
e.append(a)
e.append(b)
e.append(c-a)
e.append(d-b)
print(min(e))