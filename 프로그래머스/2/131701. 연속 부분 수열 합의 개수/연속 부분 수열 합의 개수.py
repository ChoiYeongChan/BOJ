def solution(elements):
    n=len(elements)
    elements=elements*2
    x=set()
    for i in range(n):
        for j in range(n):
            x.add(sum(elements[j:j+i+1]))
    answer=len(x)
    return answer