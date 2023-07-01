def solution(n):
    ans=0
    x=bin(n)
    c=str(x).count('1')
    while (1):
        n+=1
        x=bin(n)
        c2=str(x).count('1')
        if c==c2:
            ans=n
            break
    return ans

