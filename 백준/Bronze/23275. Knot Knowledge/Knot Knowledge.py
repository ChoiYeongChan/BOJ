import sys
input=sys.stdin.readline
n = int(input())
x_list = list(map(int, input().split()))
y_list = list(map(int, input().split()))

for x in x_list:
    if x not in y_list:
        print(x)
        break