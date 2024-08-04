import sys
import math
input=sys.stdin.readline
a,b,v=map(int,input().split())
day=0
n=v-a
day=math.ceil(n/(a-b))+1
print(day)