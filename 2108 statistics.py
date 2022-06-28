import sys
a=int(sys.stdin.readline())
b={}
x=[]
for i in range(a):
    c=int(sys.stdin.readline())
    x.append(c)
    if c in b:
        b[c]+=1
    else:
        b[c]=1
x.sort()
avg=round(sum(x)/len(x))
print(avg)
print(x[len(x)//2])
if len(b)==1:
    print(c)
    print('0')
else:
    y=sorted(b.items(), key=lambda x: (-x[1], x[0]))[:2]
    if y[0][1]==y[1][1]:
        print(y[1][0])
    else:
        print(y[0][0])
    print(x[-1]-x[0])
