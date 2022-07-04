def solution(n, lost, reserve):
    sr=set(reserve)-set(lost)
    sl=set(lost)-set(reserve)
    for i in sr:
        if i-1 in sl:
            sl.remove(i-1)
        elif i+1 in sl:
            sl.remove(i+1)
    return n-len(sl)