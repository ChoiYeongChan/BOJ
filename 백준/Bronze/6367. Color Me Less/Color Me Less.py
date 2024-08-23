li = [list(map(int, input().split())) for _ in range(16)]
while 1:
    R, G, B = map(int, input().split())
    if R == G == B == -1:
        break
    li.sort(key=lambda X:((R-X[0])**2 + (G-X[1])**2 + (B-X[2])**2))
    print('(', end='')
    print(*[R, G, B], sep=',', end='')
    print(") maps to (", end='')
    print(*li[0], sep=',', end=')\n')