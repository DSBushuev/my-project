N, M = map(int, input().split())
G = []
for i in range(N):
    G.append(list(map(int, input().split())))
def step(G,start,n):
    y,x = start
    right = left = x
    up = down = y

    while right < M:
        if G[y][right] == 2:
            print(n)
            exit()
        if G[y][right] == 1:
            right -= 1
            break
        if right == M-1:
            break
        right += 1

    while left > -1:
        if G[y][left] == 2:
            print(n)
            exit()
        if G[y][left] == 1:
            left += 1
            break
        if left == 0:
            break
        left -= 1

    while up > -1:
        if G[up][x] == 2:
            print(n)
            exit()
        if G[up][x] == 1:
            up += 1
            break
        if up < 1:
            break
        up -= 1

    while down < N:
        if G[down][x] == 2:
            print(n)
            exit()
        if G[down][x] == 1:
            down -= 1
            break
        if down == N-1:
            break
        down += 1

    res = []
    for y_, x_ in [(y, right), (y, left), (up, x), (down, x)]:
        if (y_, x_) != start:
            res.append((y_, x_))
    return res

q = [(0,0)]
n = 1
while q:
    new_q = []
    for y,x in q:
        s = step(G, (y,x), n)
        for node in s:
            new_q.append(node)
    q = new_q
    n += 1



