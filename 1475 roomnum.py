import sys
import math
input=sys.stdin.readline
n=input().rstrip()
room=[0]*10
for i in n:
    if i=='9':
        room[6]+=1
    else:
        room[int(i)]+=1
room[6]=math.ceil(room[6]/2)
print(max(room))