start = []
N, M = map(int, input().split())
for i in range(N):
    start += [(i, n) for n,x in enumerate(input().split()) if x == '1']
visited = set(start)
G = [[0 for i in range(M)] for j in range(N)]

def steps(g,x,y,n):
    global N
    global M
    global visited
    q = []
    if x > 0 and (x - 1, y) not in visited:
        visited.add((x - 1, y))
        q.append((x - 1, y))
        g[x-1][y] = n
    if x < (N - 1) and (x + 1, y) not in visited:
        visited.add((x + 1, y))
        q.append((x + 1, y))
        g[x+1][y] = n
    if y > 0 and (x, y - 1) not in visited:
        visited.add((x, y - 1))
        q.append((x, y - 1))
        g[x][y-1] = n
    if y < (M - 1) and (x, y + 1) not in visited:
        visited.add((x, y + 1))
        q.append((x, y + 1))
        g[x][y+1] = n
    return q

n = 1
while start:
    new_start = []
    for i, j in start:
        new_start += steps(G, i, j, n)
    start = new_start
    n += 1
for s in G:
    print(*s)
