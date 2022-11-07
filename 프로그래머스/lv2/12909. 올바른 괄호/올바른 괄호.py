def solution(s):
    answer=True
    a=[]
    for i in s:
        if i=='(':
            a.append('(')
        else:
            if len(a)>0:
                a.pop()
            else:
                answer=False
                break
    if len(a)>0:
        answer=False    

    return answer