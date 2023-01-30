start = tuple(map(int, input().split()))

def step(start_):
    x,y = start_
    res = []
    if x < 8 and y < 8:
        res.append((x + 1,y + 1))
    if x > 1 and y < 8:
        res.append((x - 1,y + 1))
    return res


q = [start]
while q:
    new_q = q[:]
    q = []
    for s in new_q:
        if step(s):
            q.append(step(s)[0])
        if len(step(s)) > 1:
            q.append(step(s)[1])

print(len(new_q))




