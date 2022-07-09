import sys
input=sys.stdin.readline
n=int(input())
a=[]
b=[]
s=0
for _ in range(n):
    x=int(input())
    if x>1:
        a.append(x)
    elif x==1:
        s+=1
    else:
        b.append(x)
a.sort(reverse=True)
b.sort()
if len(a)%2==0:
    for i in range(0, len(a),2):
        s+=a[i]*a[i+1]
else:
    for i in range(0,len(a)-1,2):
        s+=a[i]*a[i+1]
    s+=a[-1]
if len(b)%2==0:
    for i in range(0,len(b),2):
        s+=b[i]*b[i+1]
else:
    for i in range(0,len(b)-1,2):
        s+=b[i]*b[i+1]
    s+=b[-1]
print(s)