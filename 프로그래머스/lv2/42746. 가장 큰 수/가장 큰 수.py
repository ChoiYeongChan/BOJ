def solution(numbers):
    for i in range(len(numbers)):
        numbers[i]=str(numbers[i])
    numbers.sort(key=lambda num: num*3, reverse=True)
    ans=str(int(''.join(numbers)))
    return ans
