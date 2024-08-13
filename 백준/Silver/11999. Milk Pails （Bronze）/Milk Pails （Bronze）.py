import sys
input=sys.stdin.readline
x, y, m = map(int, input().split())

ans = 0
for i in range(1001):
    for j in range(1001):
        if x * i + y * j <= m:
            ans = max(ans, x * i + y * j)

print(ans)
