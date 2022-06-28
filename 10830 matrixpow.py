import sys
input=sys.stdin.readline
n,b=map(int,input().split())
a=[]
for _ in range(n):
    a.append(list(map(int,input().split())))

def mmul(ma,mb):
    temp=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                temp[i][j]+=ma[i][k]*mb[k][j]
            temp[i][j]%=1000
    return temp

def po(mat,num):
    if num==1:
        return mat
    if num%2==0:
        temp=po(mat,num/2)
        return mmul(temp,temp)
    else:
        temp=po(mat,num-1)
        return mmul(temp,mat)

result=po(a,b)
for i in range(n):
    for j in range(n):
        print(result[i][j]%1000,end=' ')
    print()
