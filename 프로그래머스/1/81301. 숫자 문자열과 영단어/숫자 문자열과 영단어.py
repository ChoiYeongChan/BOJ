def solution(s):
    answer = ""
    tmp=""
    arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in s:
        if i.isnumeric():
            answer+=i
        else:
            tmp+=i
            if tmp in arr:
                answer+=str(arr.index(tmp))
                tmp=""
    return int(answer)