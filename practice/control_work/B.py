N, M = map(int, input().split())
G = {i:0 for i in range(N)}
for i in range(M):
    v1, v2 = map(int, input().split())
    G[v1] += 1
    G[v2] += 1
print("YES" if max(G.values()) == min(G.values()) else "NO")