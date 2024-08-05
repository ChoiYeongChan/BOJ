import sys
input=sys.stdin.readline
def roundUp(num):
    if num-int(num)>=0.5:
        return int(num)+1
    else:
        return int(num)
n=int(input())
arr=[]
if n==0:
    print(0)
else:
    arr=[]
    for _ in range(n):
        arr.append(int(input()))
    arr.sort()
    num=roundUp(n*0.15)
    arr=arr[num:n-num]
    print(roundUp(sum(arr)/len(arr)))