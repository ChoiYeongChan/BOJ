import sys
input=sys.stdin.readline
S=list(map(str,input().rstrip()))
T=list(map(str,input().rstrip()))
while len(S) != len(T):
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.pop()
        T = T[::-1]

if S == T:
    print(1)
else:
    print(0)