n, m = map(int, input().split())
G = [[float("inf") for i in range(n)] for j in range(n)]
for i in range(m):
    v1, v2, price = map(int, input().split())
    G[v1][v2] = price
    G[v2][v1] = price

for i in range(n):
    G[i][i] = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            if G[k][i] + G[k][j] < G[i][j]:
                G[i][j] = G[j][i] = G[k][i] + G[k][j]
print(list(map(sum, G)).index(min(list(map(sum, G)))))
