import math
def solution(n, k):
    x=[i for i in range(1,n+1)]
    stack=[]
    k-=1
    
    while x:
        a=k//math.factorial(n-1)
        stack.append(x[a])
        del x[a]
        
        k=k%math.factorial(n-1)
        n-=1
    return stack