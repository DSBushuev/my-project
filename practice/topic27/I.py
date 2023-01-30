green, red = input().split()

if green == red:
    print(0)
    exit()

if (ord(list(green)[0]) + int(list(green)[1]) + ord(list(red)[0]) + int(list(red)[1])) % 2:
    print(-1)
    exit()

letters = 'abcdefgh'
numbers = '12345678'
board = [[l + n for n in numbers] for l in letters][::-1]


def steps(s):
    x, y = s
    ne = ''.join([chr(ord(x)+2), str(int(y)+1)])
    en = ''.join([chr(ord(x)+1), str(int(y)+2)])
    es = ''.join([chr(ord(x)-1), str(int(y)+2)])
    se = ''.join([chr(ord(x)-2), str(int(y)+1)])
    sw = ''.join([chr(ord(x)-2), str(int(y)-1)])
    ws = ''.join([chr(ord(x)-1), str(int(y)-2)])
    wn = ''.join([chr(ord(x)+1), str(int(y)-2)])
    nw = ''.join([chr(ord(x)+2), str(int(y)-1)])
    possible_move = [ne, en, es, se, sw, ws, wn, nw]
    impossible_move = []
    if int(y) < 3:
        impossible_move.append(ws)
        impossible_move.append(wn)
    if int(y) < 2:
        impossible_move.append(sw)
        impossible_move.append(nw)
    if int(y) > 5:
        impossible_move.append(en)
        impossible_move.append(es)
    if int(y) > 6:
        impossible_move.append(ne)
        impossible_move.append(se)
    if x < 'b':
        impossible_move.append(es)
        impossible_move.append(ws)
    if x < 'c':
        impossible_move.append(se)
        impossible_move.append(sw)
    if x > 'f':
        impossible_move.append(nw)
        impossible_move.append(ne)
    if x > 'g':
        impossible_move.append(wn)
        impossible_move.append(en)

    possible_step = [i for i in possible_move if i not in impossible_move]
    return possible_step


q = [red]
visited = set()
step = 1
while green not in q:
    new_q = []
    while q:
        new_step = q.pop()
        visited.add(new_step)
        for move in steps(new_step):
            if move in visited:
                continue
            new_q.append(move)
    q = new_q
    step += 1
print(step // 2)

