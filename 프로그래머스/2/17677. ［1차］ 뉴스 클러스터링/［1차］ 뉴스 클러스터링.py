from collections import Counter
def solution(str1, str2):
    str1=str1.lower()
    str2=str2.lower()
    str1_lst=[]
    str2_lst=[]
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            str1_lst.append(str1[i]+str1[i+1])
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            str2_lst.append(str2[i]+str2[i+1])
    counter1=Counter(str1_lst)
    counter2=Counter(str2_lst)
    inner=list((counter1&counter2).elements())
    union=list((counter1|counter2).elements())
    if len(union) == 0 and len(inner) == 0:
        return 65536
    else:
        return int(len(inner) / len(union) * 65536)