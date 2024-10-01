def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    mm,ss=map(int,pos.split(':'))
    s=ss+60*mm
    mm,ss=map(int,video_len.split(':'))
    end=ss+60*mm
    mm,ss=map(int,op_start.split(':'))
    ops=ss+60*mm
    mm,ss=map(int,op_end.split(':'))
    ope=ss+60*mm
    for i in commands:
        if ops<=s<=ope:
            s=ope
        if i =="next":
            s+=10
            if s>end:
                s=end
        else:
            s-=10
            if s<0:
                s=0
    if ops<=s<=ope:
            s=ope 
    ss=s%60
    mm=s//60
    if len(str(ss))==1:
        ss='0'+str(ss)
    if len(str(mm))==1:
        mm='0'+str(mm)
    answer=str(mm)+':'+str(ss)
    return answer