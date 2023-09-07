from collections import deque
def solution(cacheSize, cities):
    answer = 0
    if cacheSize==0:
        answer=len(cities)*5
    else:
        c=["" for _ in range(cacheSize)]
        c=deque(c)
        cities=deque(cities)
        while cities:
            city=cities.popleft().lower()
            if city in c:
                c=list(c)
                c.pop(c.index(city))
                c.append(city)
                c=deque(c)
                answer+=1
            else:
                c.popleft()
                c.append(city)
                answer+=5
    return answer