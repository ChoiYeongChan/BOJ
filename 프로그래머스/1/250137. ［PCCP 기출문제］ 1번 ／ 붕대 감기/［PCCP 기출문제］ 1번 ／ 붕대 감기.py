def solution(bandage, health, attacks):
    answer = 0
    t=bandage[0]
    x=bandage[1]
    y=bandage[2]
    now=health
    now_time=0
    for i in attacks:
        attack_time=i[0]
        damage=i[1]
        if now<health:
            time=attack_time-now_time-1
            now+=time*x
            if time>=t:
                now+=(time//t)*y
        if now>health:
            now=health
        now-=damage
        if now<=0:
            return -1
        now_time=attack_time
    if now<=0:
        answer=-1
    else:
        answer=now
    return answer