def solution(diffs, times, limit):
    start=1
    end=max(diffs)
    answer=end
    mid=0
    while start<=end:
        t=0
        mid=(start+end)//2
        n=len(diffs)
        for i in range(n):
            if mid<diffs[i]:
                t+=(times[i-1]+times[i])*(diffs[i]-mid)+times[i]
            else:
                t+=times[i]
        if t<=limit:
            end=mid-1
            answer=mid
        else:
            start=mid+1
    return answer