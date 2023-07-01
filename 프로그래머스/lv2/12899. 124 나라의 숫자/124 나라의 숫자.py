def solution(n):
    x=[]
    while(n):
        if(n%3==1):
            x.append('1')
            n=n//3
        elif(n%3==2):
            x.append('2')
            n=n//3
        else:
            x.append('4')
            n=n//3-1
    x.reverse()
    answer=''.join(x)
    return answer