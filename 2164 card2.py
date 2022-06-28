from collections import deque
import sys
a=int(sys.stdin.readline())
b=deque(range(1,a+1))
cnt=0
while 1:
    if len(b)==1:
        break
    elif cnt%2==0: #버리기
        b.popleft()
        cnt+=1
    elif cnt%2==1:
        c=b.popleft()
        b.append(c)
        cnt+=1
print(b[0])
