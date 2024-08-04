import sys
input=sys.stdin.readline
arr=[0]*10001
n=int(input())
for _ in range(n):
    x=int(input())
    arr[x]+=1
for i in range(10001):
    x=arr[i]
    if x!=0:
        for _ in range(x):
            print(i)