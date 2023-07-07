def solution(k, tangerine):
    dic={}
    answer = 0
    for i in range(len(tangerine)):
        if tangerine[i] in dic.keys():
            dic[tangerine[i]]+=1
        else:
            dic[tangerine[i]]=1
    a=sorted(dic.items(),key=lambda x:x[1],reverse=True)
    for i in range(len(a)):
        k-=a[i][1]
        answer+=1
        if k<=0:
            break
    return answer