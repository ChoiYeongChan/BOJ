import sys
input=sys.stdin.readline
index = int(input())
count = 0

for _ in range(index):
    str_input = input()
    rst = str_input.lower()
    if "rose" in rst or "pink" in rst:
        count += 1

if count > 0:
    print(count)
else:
    print("I must watch Star Wars with my daughter")