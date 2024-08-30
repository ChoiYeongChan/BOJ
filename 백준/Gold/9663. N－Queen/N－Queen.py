import sys
input=sys.stdin.readline
n=int(input())
ans=0
row=[0]*n
def is_queen(x):
    for i in range(x):
        if row[x]==row[i] or abs(row[x]-row[i])==abs(x-i):
            return False
    return True
def nqueen(x):
    global ans
    if x==n:
        ans+=1
        return
    else:
        for i in range(n):
            row[x]=i
            if is_queen(x):
                nqueen(x+1)
nqueen(0)
print(ans)