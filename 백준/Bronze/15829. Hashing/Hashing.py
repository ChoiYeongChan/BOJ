import sys
a=int(sys.stdin.readline())
b=list(sys.stdin.readline().rstrip())
#a=97
sum=0
for i in range(len(b)):
    sum+=(ord(b[i])-96)*(31**i)
print(sum%1234567891)