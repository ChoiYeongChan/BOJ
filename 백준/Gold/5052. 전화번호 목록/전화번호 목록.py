import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    phone=[]
    for _ in range(n):
        phone.append(input().rstrip())
    phone.sort()
    flag=0
    for i in range(len(phone)-1):
        if phone[i]==phone[i+1][0:len(phone[i])]:
            print('NO')
            flag=1
            break
    if flag==0:
        print('YES')
