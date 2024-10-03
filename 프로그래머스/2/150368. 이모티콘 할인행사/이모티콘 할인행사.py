from itertools import product
def solution(users, emoticons):
    discount=list(product([10,20,30,40],repeat=len(emoticons)))
    ans_eplus=0
    ans_profit=0
    for d in discount:
        eplus=0
        profit=0
        for rate,price in users:
            total_price=0
            for i in range(len(emoticons)):
                if d[i]>=rate:
                    total_price+=((100-d[i])*emoticons[i])/100
                    if total_price>=price:
                        eplus+=1
                        break
            else:
                profit+=total_price
                continue
        if eplus>ans_eplus:
            ans_eplus=eplus
            ans_profit=profit
        elif eplus==ans_eplus:
            ans_profit=max(profit,ans_profit)
    return [ans_eplus,ans_profit]