def dfs(idx,result):
    global mi
    global ma
    if idx==N-1:
        if ma<=result:
            ma=result
        if result<=mi:
            mi=result
        return

    for i in range(4):
        if op[i]>0:
            op[i]-=1
            if i==0:
                new_res=result+num[idx+1]
            elif i==1:
                new_res=result-num[idx+1]
            elif i==2:
                new_res=result*num[idx+1]
            else:
                new_res=int(result/num[idx+1])
            dfs(idx+1,new_res)
            op[i]+=1

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    ma=-100000001
    mi=100000001
    N=int(input())
    op=list(map(int,input().split()))
    num=list(map(int,input().split()))
    dfs(0,num[0])
    print('#'+str(test_case),ma-mi)