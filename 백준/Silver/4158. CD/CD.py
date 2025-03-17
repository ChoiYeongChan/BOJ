import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    dic = set()
    for _ in range(n):
        cd = int(input())
        dic.add(cd)

    cnt = 0
    for _ in range(m):
        cd = int(input())
        if cd in dic:
            cnt += 1

    print(cnt)
