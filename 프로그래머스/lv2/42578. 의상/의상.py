def solution(clothes):
    dic={}
    answer=1
    for i in range(len(clothes)):
        key=clothes[i][1]
        value=clothes[i][0]
        if key in dic:
            dic[key].append(value)
        else:
            dic[key]=[value]
    for key in dic.keys():
        answer=answer*(len(dic[key])+1)
    return answer-1