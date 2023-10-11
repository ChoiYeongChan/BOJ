import sys
import copy
def combinations(array,r):
    for i in range(len(array)):
        if r ==1:
            yield [array[i]]
        else:
            for next in combinations(array[i+1:],r-1):
                yield[array[i]]+next
def move():
    for i in range(-1,-N,-1):
        temp[i]=temp[i-1]
    temp[0]=[0 for _ in range(M)]
def is_empty():
    for i in range(N):
        for j in range(M):
            if temp[i][j]==1:
                return False
    return True
def attack(li):
    attack_list=[]
    cnt=0
    for l in li:
        pos=[]
        for i in range(N):
            for j in range(M):
                if temp[i][j]==1:
                    distance=abs(i-N)+abs(j-l)
                    if D>=distance:
                        pos.append((distance,i,j))
        pos.sort(key=lambda x:(x[0],x[2]))
        if pos:
            attack_list.append(pos[0])
    
    for a in attack_list:
        _,i,j=a
        if temp[i][j]==1:
            temp[i][j]=0
            cnt+=1
    return cnt
input=sys.stdin.readline
N,M,D=map(int,input().split())
board=[]
for _ in range(N):
    board.append(list(map(int,input().split())))
x=[i for i in range(0,M)]
ans=0
for a in combinations(x,3):
    temp=copy.deepcopy(board)
    cnt=0
    while not is_empty():
        cnt+=attack(a)
        move()
    ans=max(ans,cnt)
print(ans)