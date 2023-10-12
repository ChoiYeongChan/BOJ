T=int(input())
for test_case in range(1,T+1):
    N,K=map(int,input().split())
    s=input().rstrip()
    arr=set()
    for _ in range(N//4):
        for i in range(0,N,N//4):
            arr.add(s[i:i+N//4])
        
        s=s[-1]+s[:-1]
    arr=list(arr)
    arr.sort(reverse=True)
    res=arr[(K-1)%len(arr)]    
    print('#'+str(test_case),int(res,16))