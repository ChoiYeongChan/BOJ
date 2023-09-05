def solution(s):
    answer = []
    s=s[2:-2]
    x=list(s.split("},{"))
    x.sort(key=len)
    for i in x:
        y=i.split(",")
        while y:
            n=int(y.pop())
            if n not in answer:
                answer.append(n)
    
    return answer