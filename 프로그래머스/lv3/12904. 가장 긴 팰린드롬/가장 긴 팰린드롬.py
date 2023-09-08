def solution(s):
    answer = 1
    if len(s)==1:
        return 1
    for i in range(0,len(s)):
        for j in range(i+1,len(s)+1):
            pal=s[i:j]
            if len(pal)%2==0:
                n=len(pal)//2
                pal1=pal[0:n]
                pal2=pal[n:len(pal)]
                pal2=pal2[::-1]
                if pal1==pal2:
                    answer=max(answer,len(pal))
            else:
                n=len(pal)//2      
                pal1=pal[0:n]
                pal2=pal[n+1:len(pal)]
                pal2=pal2[::-1]
                if pal1==pal2:
                    answer=max(answer,len(pal))
    return answer