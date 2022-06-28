n=int(input())
tile=[1,3,5]
for i in range(3,1001):
    tile.append(tile[i-2]*2 + tile[i-1])
print(tile[n-1]%10007)