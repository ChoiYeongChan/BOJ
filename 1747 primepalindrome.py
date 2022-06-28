import sys
import math
input=sys.stdin.readline
def isPrime(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True

n=int(input())
palin=0
for i in range(n,1000001):
    if i==1:
        continue
    if str(i)==str(i)[::-1]:
        if isPrime(i)==True:
            palin=i
            break

if palin==0:
    palin=1003001
print(palin)