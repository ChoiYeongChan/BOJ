from itertools import permutations
def solution(numbers):
    answer = 0
    x=list(numbers)
    s=set()
    for i in range(len(x)):
        p=list(set(permutations(x,i+1)))
        for j in range(len(p)):
            a=""
            for k in range(len(p[j])):
                a+=p[j][k]
                s.add(int(a))
    s=list(s)
    prime=[False,False]+[True]*(10**(len(x)))
    for i in range(2,len(prime)):
        if prime[i]:
            for j in range(2*i, len(prime), i):
                prime[j] = False
    for i in s:
        if prime[i]:
            answer+=1
    return answer