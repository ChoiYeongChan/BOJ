def solution(lottos, win_nums):
    answer = []
    cnt=0
    co=0
    for i in lottos:
        if i==0:
            cnt+=1
            co+=1
        else:
            if i in win_nums:
                co+=1
    l=[6,6,5,4,3,2,1]
    answer.append(l[co])
    answer.append(l[co-cnt])
    return answer