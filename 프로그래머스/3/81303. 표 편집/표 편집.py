def solution(n, k, cmd):
    cur=k
    table = { i:[i - 1, i + 1] for i in range(n) }
    answer = ['O'] * n
    table[0] = [None, 1]
    table[n - 1] = [n - 2, None]
    stack=[]
    for i in cmd:
        if i=='C':
            answer[cur] = 'X'
            prev, next = table[cur]
            stack.append([prev,cur,next])
            if next==None:
                cur=table[cur][0]
            else:
                cur=table[cur][1]
            if prev == None:
                table[next][0] = None
            elif next == None:
                table[prev][1] = None
            else:
                table[prev][1] = next
                table[next][0] = prev
        elif i=='Z':
            prev, now, next = stack.pop()
            answer[now] = 'O'
            if prev == None:
                table[next][0] = now
            elif next == None:
                table[prev][1] = now
            else:
                table[next][0] = now
                table[prev][1] = now
        else:
            c,n=i.split(' ')
            n=int(n)
            if c=='D':
                for _ in range(n):
                    cur=table[cur][1]
            else:
                for _ in range(n):
                    cur=table[cur][0]
    return ''.join(answer)