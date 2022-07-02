def solution(participant, completion):
    hashD={}
    sumHash=0
    for i in participant:
        hashD[hash(i)]=i
        sumHash+=hash(i)
    for i in completion:
        sumHash-=hash(i)
        
    return hashD[sumHash]