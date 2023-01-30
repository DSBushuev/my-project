s = input()
i = 0
j = 1
n = 0
res = 0
flag = True
while j < len(s):
    if s[i] == s[j]:
        i += 1
        j += 1
        n += 1
        if len(s)/n == n and res < n:
            res = n
    elif i == 0:
        flag = False
        j += 1
    else:
        flag = False
        if len(s)/n == n and res < n:
            res = n
if res:
    print(res,"!")
    exit()
if flag:
    print(len(s))


