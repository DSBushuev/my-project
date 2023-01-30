N = int(input())
G = []
for i in range(N):
    G.append(list(map(int, input().split())))
out = []
inp = []
for i in range(N):
    if sum(G[i]) == 0:
        out.append(i+1)
    flag = True
    for j in range(N):
        if G[j][i]:
            flag = False
            break
    if flag:
        inp.append(i+1)
print(*inp)
print(*out)



