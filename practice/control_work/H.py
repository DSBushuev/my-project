from collections import deque


n, m, *capitals = map(int, input().split())
roads = {}
def roads_add(s1,s2,d):
    global roads
    if s1 not in roads:
        roads[s1] = {s2: distance}
    else:
        roads[s1][s2] = distance


for i in range(m):
    s1, s2, distance = map(int, input().split())
    roads_add(s1,s2,distance)
    roads_add(s2,s1,distance)

def search_min_distance(G, start, finish):
    min_distance = {start: 0}
    q = deque()
    q.append(start)
    while q:
        vertex = q.popleft()
        if vertex not in G:
            continue
        for v in G[vertex]:
            if v not in min_distance or min_distance[v] > min_distance[vertex] + G[vertex][v]:
                min_distance[v] = min_distance[vertex] + G[vertex][v]
                q.append(v)
    return min_distance[finish] if finish in min_distance else float("inf")

res = []
for city in range(n):
    if city in capitals:
        res.append(city)
        continue
    if city not in roads:
        res.append(-1)
        continue
    my_distance = float("inf")
    my_capital = -1
    for capital in capitals:
        min_distance = search_min_distance(roads, capital, city)
        if min_distance < my_distance:
            my_distance = min_distance
            my_capital = capital
    res.append(my_capital)
print(*res, sep="\n")











