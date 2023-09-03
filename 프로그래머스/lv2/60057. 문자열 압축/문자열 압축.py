from collections import deque
def solution(s):
    answer = len(s)
    n=0
    if (len(s)%2==0):
        n=len(s)//2
    else:
        n=len(s)//2+1
    n+=1
    for i in range(1,n):
        result=deque([s[j:j+i] for j in range(0, len(s), i)])
        x=""
        while(result):
            a=result.popleft()
            cnt=1
            while(result):
                b=result.popleft()
                if a==b:
                    cnt+=1
                else:
                    result.appendleft(b)
                    break
            if cnt==1:
                x+=a
            else:
                x+=str(cnt)+a
        if len(x)<answer:
            answer=len(x)
    return answer