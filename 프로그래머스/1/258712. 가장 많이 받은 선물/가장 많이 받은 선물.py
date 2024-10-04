def solution(friends, gifts):
    answer = 0
    n=len(friends)
    dic={}
    for i in range(n):
        dic[friends[i]]=i
    present=[[0 for _ in range(n)] for _ in range(n)]
    for i in gifts:
        a,b=i.split(" ")
        present[dic[a]][dic[b]]+=1
    pp=[]
    for i in range(n):
        cnt=0
        for j in range(n):
            cnt+=present[i][j]
            cnt-=present[j][i]
        pp.append(cnt)
    total=[0]*n
    for i in range(n):
        for j in range(n):
            if j>i:
                if present[i][j]<present[j][i]:
                    total[j]+=1
                elif present[i][j]==present[j][i]:
                    if pp[i]>pp[j]:
                        total[i]+=1
                    elif pp[j]>pp[i]:
                        total[j]+=1
                else:
                    total[i]+=1
    return max(total)