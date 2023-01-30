import time

start = input()
stop = input()
start_time = time.perf_counter()
max_start = max(list(map(int, list(start))))
min_start = min(list(map(int, list(start))))
max_stop = max(list(map(int, list(stop))))
min_stop = min(list(map(int, list(stop))))
maximum = max(max_stop, max_start)
minimum = min(min_stop, min_start)
if stop == start:
    print(int(start), int(stop), sep='\n')
    exit()
def step(number:str,max_, min_):
    res = []
    if int(number[0]) < max_:
        res.append(str(int(number) + 1000))
    if int(number[-1]) > min_:
        res.append(str(int(number)-1))
    res.append(number[3]+number[:3])
    res.append(number[1:]+number[0])
    return res

parrents = {}
q = [start]
visited = set()

def print_way(n, p):
    res = []
    while start not in res:
        res.append(p[n])
        n = p[n]
    res = list(map(int, res[::-1])) + [int(stop)]
    print(*res, sep="\n")
    end_time = time.perf_counter()
    print(f'{end_time - start_time:.8f}')
    exit()

n = 1
while q:
    n += 1
    if not n % 10000:
        print(n)
    new_start = q.pop(0)
    visited.add(new_start)
    for next_start in step(new_start, maximum, minimum):
        if next_start in visited:
            continue
        if next_start not in parrents:
            q.append(next_start)
            parrents[next_start] = new_start
        if next_start == stop:
            print_way(next_start, parrents)









