import sys
input=sys.stdin.readline
l = []
for _ in range(3):
    l.append(int(input()))
l.sort()
print(l[1])