import sys
input=sys.stdin.readline
a,b=map(str,input().split())
x= int(a.replace('6', '5')) + int(b.replace('6', '5'))
y = int(a.replace('5', '6')) + int(b.replace('5', '6'))
print(x,y)