def solution(number, k):
    number=list(number)
    res=[number.pop(0)]
    for n in number:
        if res[-1]<n:
            while res and res[-1]<n and k>0:
                res.pop()
                k-=1
            res.append(n)
        elif k==0 or res[-1]>=n:
            res.append(n)
    if k:
        res=res[:-k]
    answer=''.join(res)
    return answer