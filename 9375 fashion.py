import sys
n=int(sys.stdin.readline())
for _ in range(n):
    m=int(sys.stdin.readline())
    cloth={}
    for _ in range(m):
        a,b=sys.stdin.readline().rstrip().split()
        if b in cloth:
            cloth[b].append(a)
        else:
            cloth[b]=[]
            cloth[b].append(a)
    sum=1
    for key in cloth:
        sum*=(len(cloth[key])+1)
    print(sum-1)