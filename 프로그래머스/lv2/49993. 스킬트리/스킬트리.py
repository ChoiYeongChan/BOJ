def solution(skill, skill_trees):
    answer=0
    for i in skill_trees:
        x=[]
        for j in range(len(skill)):
            try:
                a=i.index(skill[j])
                x.append(a)
            except:
                x.append(-1)
        while(1):
            if len(x)==0:
                break
            if x[-1]==-1:
                x.pop()
            else:
                break
        if len(x)>0:
            y=sorted(x)
            if x==y and y[0]!=-1:
                answer+=1
        else:
            answer+=1        
    return answer