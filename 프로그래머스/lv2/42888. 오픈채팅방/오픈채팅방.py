def solution(record):
    answer=[]
    dic={}
    s=[]
    for i in record:
        a=i.split(" ")
        if a[0]=="Enter":
            dic[a[1]]=a[2]
            s.append(a)
        elif a[0]=="Change":
            dic[a[1]]=a[2]
        elif a[0]=="Leave":
            s.append(a)
    for i in s:
        if i[0]=="Enter":
            answer.append(dic[i[1]]+"님이 들어왔습니다.")
        else:
            answer.append(dic[i[1]]+"님이 나갔습니다.")
    return answer