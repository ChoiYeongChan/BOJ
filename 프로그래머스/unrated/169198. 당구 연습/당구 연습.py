def solution(m, n, startX, startY, balls):
    answer = []
    for i in range(len(balls)):
        dists=[]
        ballX=balls[i][0]
        ballY=balls[i][1]
        if not (ballX == startX and ballY > startY):
            d2 = (ballX - startX)**2 + (ballY - 2*n+startY)**2
            dists.append(d2)
        if not (ballX == startX and ballY < startY):
            d2 = (ballX - startX)**2 + (ballY + startY)**2
            dists.append(d2)
        if not (ballY == startY and ballX < startX):
            d2 = (ballX + startX)**2 + (ballY - startY)**2
            dists.append(d2)
        if not (ballY == startY and ballX > startX):
            d2 = (ballX - 2*m+startX)**2 + (ballY - startY)**2
            dists.append(d2)
        answer.append(min(dists))
    return answer