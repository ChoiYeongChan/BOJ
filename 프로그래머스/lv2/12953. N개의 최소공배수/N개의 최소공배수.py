import math
def solution(arr):
    answer = 0
    if len(arr)==1:
        answer=arr[0]
    else:
        arr.sort()
        l=1
        for i in arr:
            l=(l*i)//(math.gcd(l,i))
        answer=l
    return answer