import sys
A=sys.stdin.readline().rstrip()
B=sys.stdin.readline().rstrip()

x=len(A)
y=len(B)
matrix=[[0]*(y+1) for _ in range(x+1)]

for i in range(1, x+1):
    for j in range(1,y+1):
        if A[i-1]==B[j-1]:
            matrix[i][j]=matrix[i-1][j-1]+1
        else:
            matrix[i][j]=max(matrix[i-1][j],matrix[i][j-1])

print(matrix[-1][-1])