import math
def solution(n, words):
    answer = []
    x=[]
    a=0
    b=0
    x.append(words[0])
    for i in range(1,len(words)):
        if words[i-1][-1]!=words[i][0] or words[i] in x:
            i+=1
            a=math.ceil(i/n)
            b=i%n
            if b==0:
                b=n
            break
        else:
            x.append(words[i])
    answer.append(b)
    answer.append(a)
    return answer