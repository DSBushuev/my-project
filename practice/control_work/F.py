M, N = map(int, input().split())
order = {}
for i in range(N):
    s1, s2 = map(int, input().split())
    if s1 not in order:
        order[s1] = [s2]
    else:
        if s2 not in order[s1]:
            order[s1].append(s2)

stack = []
V = set()

def serch_loop(G,v,stack,V):
    V.add(v)
    if v in G and G[v]:
        vertex = G[v].pop()
        stack.append(v)
        if vertex in stack:
            print("NO")
            exit()
        if vertex in V:
            v = stack.pop()
            serch_loop(G, v, stack, V)
        else:
            serch_loop(G, vertex, stack, V)
    else:
        if stack:
            vertex = stack.pop()
            serch_loop(G, vertex, stack, V)

for s in order:
    if s in V:
        continue
    if order[s]:
        serch_loop(order, s, stack, V)

print("YES")