import sys
input=sys.stdin.readline
n=int(input())
li=set()
for _ in range(n):
    li.add(input().rstrip())
li=list(li)
li.sort(key=lambda x:(len(x),x))
for i in li:
    print(i)