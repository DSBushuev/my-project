n, m = input().split()
G = {}
values = set()
keys = set()
for i in range(int(m)):
    x, y = input().split()
    values.add(y)
    keys.add(x)
    if x not in G:
        G[x] = [y]
    else:
        G[x].append(y)
bad_values = [i for i in list(values) if i in keys]
result = [0]*(int(m)+1)

def search_road(graph, stop, start):
    res = [start]
    while start != stop:
        if start in graph:
            start = graph[start]
            res.append(start)
        else:
            return None
    return res

def search_loop(graph, start):
    global bad_values
    parents = {}
    visited = set()
    q = [start]
    while q:
        new_start = q.pop(0)
        if new_start not in bad_values:
            continue
        if new_start in visited:
            continue
        visited.add(new_start)
        if new_start not in graph:
            continue
        for next_start in graph[new_start]:
            if next_start in visited:
                parents[next_start] = new_start
                if new_start in parents:
                    return search_road(parents, next_start, new_start)
            elif next_start not in parents:
                parents[next_start] = new_start
                q.append(next_start)

for node in values:
    res = search_loop(G, node)
    if res and len(res) < len(result):
        result = res
if len(result) == int(m)+1:
    print("NO CYCLES")
    exit()
print(*result)







