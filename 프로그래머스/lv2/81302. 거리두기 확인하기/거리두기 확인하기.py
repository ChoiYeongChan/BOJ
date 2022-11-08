dx=[0,0,1,-1]
dy=[1,-1,0,0]
def BFS(x,y,room):
    visited=[[0 for _ in range(5)] for _ in range(5)]
    man=0
    start=[[x,y]]
    man_len=[0]
    
    while start:
        x=start[0][0]
        y=start[0][1]
        start.remove(start[0])
        visited[x][y]=1
        man=man_len[0]
        man_len.remove(man_len[0])
        if man==2:
            return 1

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<5 and 0<=ny<5 and visited[nx][ny]==0:
                if room[nx][ny]=='P':
                    return 0
                elif room[nx][ny]=='O':
                    start.append([nx,ny])
                    man_len.append(man+1)
    return 1
def solution(places):
    answer=[]
    for room in places:
        stop=False
        for x in range(5):
            for y in range(5):
                if room[x][y]=='P':
                    if BFS(x,y,room)==0:
                        stop=True
                        break
            if stop==True:
                break
        if stop==True:
            answer.append(0)
        else:
            answer.append(1)
    return answer