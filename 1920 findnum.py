import sys
def binary_search(target,data):
    start=0
    end=len(b)-1
    while start<=end:
        mid=int((start+end)/2)
        if b[mid]==target:
            print("1")
            return
        elif b[mid]<target:
            start=mid+1
        else:
            end=mid-1
    print("0")
    return
a=int(sys.stdin.readline())
b=[]
b=list(map(int,sys.stdin.readline().split()))
b.sort()
c=int(sys.stdin.readline())
d=[]
d=list(map(int,sys.stdin.readline().split()))
for i in range (c):
    binary_search(d[i],b)